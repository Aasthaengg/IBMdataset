from bisect import bisect_left, bisect_right
N = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0
for i in range(N-1, 1, -1):
    for j in range(i - 1, 0, -1):
        x = L[i] - L[j]
        bottom = bisect_right(L, x)
        if j > bottom:
            ans += j - bottom
print(ans)
