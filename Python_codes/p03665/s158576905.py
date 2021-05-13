n, p = map( int, input().split())
lis = list( map( int, input().split()))

def nCk( n, k):
  ans = 1
  for i in range(k):
    ans *= (n-i)
  for i in range(k):
    ans /= (k-i)
  return ans

e = 0
o = 0
for i in lis:
  if i % 2 == 0:
    e += 1
  else:
    o += 1

if p == 0:
  ans = 1
  for i in range( o//2):
    ans += nCk( o, (i+1)*2)
  print( int( ans * 2**e))
else:
  ans = 0
  for i in range( o//2):
    ans += nCk( o, i*2+1)
  print( int( ans * 2**e))