import sys
a,b,k = map(int,input().split())

if a >= k:
  print(a-k,b)
  sys.exit()

if b >= (k-a):
  print(0,b-(k-a))
  sys.exit()

print(0,0)