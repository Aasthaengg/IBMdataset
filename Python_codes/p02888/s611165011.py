from bisect import bisect_left

N = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0
for i in range(N):
    for j in range(i+1, N):
        x = L[i] + L[j]
        y = bisect_left(L, x)
        ans += y - j - 1
print(ans)