from itertools import accumulate

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)
a_acm = list(accumulate(a))

a_cnt = [0] * (10 ** 6 + 1)
for e in a:
    a_cnt[e] += 1

acm = list(accumulate(a_cnt))


def count_handshake(x):
    ret = 0
    for e in a:
        if x - e - 1 >= 0:
            cnt = acm[-1] - acm[x-e-1]
        else:
            cnt = n

        ret += cnt

    return ret


left = 0
right = 10 ** 6

while right - left > 1:
    mid = (left + right) // 2
    if count_handshake(mid) >= m:
        left = mid
    else:
        right = mid

ans = 0
handshake_cnt = 0
for e in a:
    if left - e - 1 >= 0:
        cnt = n - acm[left-e-1]
    else:
        cnt = n

    if cnt > 0:
        ans += e * cnt + a_acm[cnt-1]
        handshake_cnt += cnt

if handshake_cnt > m:
    ans -= left * (handshake_cnt - m)

print(ans)
