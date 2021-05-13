import sys
n = int(input())
A = list(map(int, input().split()))
A.sort()
p = 1
for i in range(n):
   p *= A[i]
   if p > 10**18:
      print(-1)
      exit()
print(p)