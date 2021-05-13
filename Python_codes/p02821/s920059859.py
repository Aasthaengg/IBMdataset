import bisect


def solve(mid):
    cnt = 0
    l = n
    r = n
    for i in range(n):
        while True:
            if l == 0:
                break
            if a[l - 1] < mid - a[i]:
                break
            l -= 1
        cnt += (r - l)
    return cnt >= m
    

n, m = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)

ok = 0
ng = 10 ** 18
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if solve(mid):
        ok = mid
    else:
        ng = mid

ru = [0] * (n + 1)
for i in range(n):
    ru[i + 1] = ru[i] + a[i]

ans = 0
r = n
ok = ok + 1
cnt = 0
for i in range(n):
    l = bisect.bisect_left(a, ok - a[i])
    cnt += (r - l)
    ans += (r - l) * a[i] + (ru[r] - ru[l])
ans += (ok - 1) * (m - cnt)
print(ans)
