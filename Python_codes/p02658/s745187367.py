import sys

N = int(input())
A = list(map(int,input().split()))

U = 10**18
ret = 1

for x in A:
  ret *= x
  if ret > U:
    ret = U+1
    
if ret > U:
  ret = -1

print(ret)