import math
N = int(input())
D,X = map(int,input().split())
ans = 0
for i in range(N):
  num = int(input())
  ans += (math.floor((D - 1) / num) + 1)
print(ans + X)