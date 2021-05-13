import sys
input = sys.stdin.readline
n = int(input())
f = [int("".join(input().split()),base=2) for _ in range(n)]
p = [list(map(int,input().split())) for _ in range(n)]
ans = -10**10

for i in range(1,1<<10):
  profit = 0
  for j in range(n):
    cnt = bin(i&f[j]).count("1")
    profit += p[j][cnt]
  ans = max(ans,profit)
print(ans)