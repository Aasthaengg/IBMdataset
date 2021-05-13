K = int(input())
import sys
num = 0
for n in range(K):
  num = num * 10 + 7
  if num % K == 0:
    print(n+1)
    break
  num = num % K
else:
  print(-1)