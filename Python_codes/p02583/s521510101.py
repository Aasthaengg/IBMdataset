from itertools import combinations
n = int(input())
l = list(map(int, input().split()))

ans = 0
for i,j,k in combinations(l,3):
  if i == j or i == k or j == k: continue
  if i >= j+k or j >= i+k or k >= i+j: continue
  ans += 1
print(ans)