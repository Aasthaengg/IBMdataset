import bisect

n, m = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A)
cumA = [0] * (n + 1)
for i in range(n):
    cumA[i+1] = cumA[i] + A[i]

ans = 0
ok, ng = 0, 1e6
while abs(ng-ok) > 1:
    mid = (ok+ng) // 2
    t = 0
    for a in A:
        t += n - bisect.bisect_left(A, mid-a)
    if t >= m: ok = mid
    else: ng = mid

ans = 0
t = 0
for i in range(n):
    k = bisect.bisect_left(A, ng - A[i])
    t += n - k
    ans += cumA[n] - cumA[k] + (n-k)*A[i]
ans += ok*(m-t)
print(int(ans))