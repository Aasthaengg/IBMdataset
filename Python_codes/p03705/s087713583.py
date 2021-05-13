import sys
n,a,b = map(int,input().split())

if a > b:
  print(0)
  sys.exit()
  
if n == 1:
  if a == b:
    print(1)
    sys.exit()
  else:
    print(0)
    sys.exit()

print((b-a)*(n-2)+1)