import sys
n,m = map(int,input().split())
if m < 2:
  print(0)
  sys.exit()
if(1 < m < n) or 2*n > m >= n:
  print(m//2)
  sys.exit()
m -= 2*n
print(n+(m//4))
