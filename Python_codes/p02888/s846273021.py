import bisect
N = int(input())
L = sorted(map(int, input().split()))
ans = 0
for i in range(N - 2):
    a = L[i]
    for j in range(i + 1, N - 1):
        b = L[j]
        kmin = bisect.bisect_left(L, (b - a), j + 1)
        kmax = bisect.bisect_left(L, (a + b), j + 1)
        ans += (kmax - kmin)
print(ans)