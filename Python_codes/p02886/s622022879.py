from itertools import combinations
N = int(input())
d = list(map(int,input().split()))
C = list(combinations(range(0,N),2))

ans = 0
for x,y in C:
  ans += d[x] * d[y]

print(ans)