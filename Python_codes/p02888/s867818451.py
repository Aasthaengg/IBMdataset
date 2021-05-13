import bisect
N = int(input())
L = list(map(int, input().split()))
L.sort()

ans = 0
for i in range(N-2):
  for j in range(i+2, N):
    a, b = L[i], L[j]
    right = bisect.bisect_right(L, b-a)
    left = max(right, i+1)
    ans += j - left
print(ans)