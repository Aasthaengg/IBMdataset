dp = {}

n = int(input())
a = [int(i) for i in input().split()]

q = int(input())
ms = [int(i) for i in input().split()]

def solve(i, m):
  global n, a

  if  (i, m) in dp:
    return dp[(i, m)]

  if m == 0:
    dp[(i, m)] = True
  elif n <= i:
    dp[(i, m)] = False
  elif solve(i + 1, m):
    dp[(i, m)] = True
  elif solve(i + 1, m - a[i]):
    dp[(i, m)] = True
  else:
    dp[(i, m)] = False
  
  return dp[(i, m)]

for m in ms:
  if solve(0, m):
    print('yes')
  else:
    print('no')

