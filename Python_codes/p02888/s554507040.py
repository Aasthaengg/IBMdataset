from bisect import bisect_right

N = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        b = L[i]
        c = L[j]
        M = L[i+1:j]
        ans += bisect_right(M, b + c - 1) - bisect_right(M, c - b)
print(ans)