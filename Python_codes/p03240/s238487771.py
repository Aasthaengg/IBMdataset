import sys
input = sys.stdin.readline
n = int(input())
c = []
for i in range(n):
  a = [int(i) for i in input().split()]
  c.append(a)

from operator import itemgetter
c = sorted(c,key=itemgetter(2),reverse=True)
p,q,r = c[0]
end = c[-1]
c = c[1:]
for i in range(101):
  for j in range(101):
    if r > 0:
      chk = abs(p-i)+abs(q-j)+r
    else:
      chk = 1
    for num,k in enumerate(c):
      x,y,h = k
      if h == 0:
        if abs(x-i)+abs(y-j) < chk:
          break
      else:
        if abs(x-i)+abs(y-j)+h != chk:
          break
      if k == end:
        ans = (i,j,chk)

print(*ans)