n = int(input())
A = []
B = []
ans = 0
import math

for _ in range(n):
  a,b = map(int,input().split())
  A.append(a)
  B.append(b)
  
for _ in range(n):
  a = A.pop(-1)
  b = B.pop(-1)
  a += ans
  ans += math.ceil(a/b)*b - a

print(ans)

