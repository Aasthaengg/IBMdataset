ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

from math import log10

n,k=nm()
a=nl()
b=[1]*(n+1)

for i in range(n):
  b[i+1] = log10(a[i])+b[i]

for i in range(n-k):
  if b[i+k+1]-b[i+1] > b[i+k]-b[i]:
    print('Yes')
  else:
    print('No')
