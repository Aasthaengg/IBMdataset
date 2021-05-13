import sys

n,m = map(int, input().split())

num = ['-'] * n

for i in range (m):
  s,c = map(int, input().split())
  if num[s-1] != '-' and num[s-1] != c:
    print('-1')
    sys.exit()
  else:
    num[s-1] = c

if n > 1:
  if num[0] == 0:
    print('-1')
    sys.exit()
  elif num[0] == '-':
    num[0] = 1 
  
for i in range(n):
  if num[i] == '-':
    num[i] = '0'
  else:
    num[i] = str(num[i])

print(''.join(num))