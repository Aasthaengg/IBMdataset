import math
N, M = map(int, input().split())
S = str(input())
T = str(input())

cnt = math.gcd(N, M)
ans = N * M // cnt
a, b = 0, 0
flag = False
for i in range(cnt):
  if S[a] != T[b]:
    flag = True
    break
  a += N//cnt
  b += M//cnt
  
if flag:
  ans = -1
print(ans)