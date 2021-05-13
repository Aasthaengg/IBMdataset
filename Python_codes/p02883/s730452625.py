def f(point):
    cnt = 0
    for i in range(N):
        a, f = A[i], F[i]
        cnt += max(0, a - point//f)
    return cnt <= K

N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))
A.sort()
F.sort(reverse=True)
l = -1
r = 10**12
while (r-l) > 1:
    mid = (r+l)//2
    if f(mid):
        r = mid
    else:
        l = mid
print(r)
