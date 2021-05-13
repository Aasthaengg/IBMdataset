import sys
n,m = map(int,input().split())
num = ['t'] * n

for i in range(m):
  j,x = map(int,input().split())
  if (j,x) == (1,0) and n != 1:
    print(-1)
    sys.exit()
  if num[j-1] == 't':
    num[j-1] = x
  elif num[j-1] != x:
    print(-1)
    sys.exit()
    
if (n,m) == (1,0):
  print(0)
  sys.exit()

for i in range(n):
  if i == 0 and num[i] == 't':
    num[0] = '1'
  elif num[i] == 't':
    num[i] = '0'
  else:
    num[i] = str(num[i])
    
print(''.join(num))   