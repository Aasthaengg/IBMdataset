_, k = map(int, input().split())
a = list(map(int, input().split()))
d = {1: 0}

k += 1
next = 1
cnt = 1
flg = True
while cnt < k:
    next = a[next - 1]
    if flg and next in d:
        flg = False
        d_next = d[next]
        loop_cnt = cnt - d_next  # 1ループの回数
        k -= ((k - d_next) // loop_cnt - 2) * loop_cnt
    d[next] = cnt
    cnt += 1
print(next)