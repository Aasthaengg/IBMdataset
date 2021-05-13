import math
n = int(input())
A = list(map(int, input().split()))

def l(x):
  k = 0
  while True:
    if x % 2==0:
      k += 1
      x = x//2
    else:
      break
  return(k)

ans = 0
for i in range(n):
  ans += l(A[i])
  
print(ans)