import math
n = int(input())

c = []
aok = 0
for i in range(n):
  a,b=map(int, input().split())
  cc  = a+b
  c.append(cc)
  aok += b
c.sort(reverse=True)

ans = sum(c[::2])-aok
print (ans)