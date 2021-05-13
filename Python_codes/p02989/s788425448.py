n = int(input())
d = [int(i) for i in input().split()]
d.sort()
r = d[int(n/2)]
l = d[int(n/2)-1]
if r == l :
  print(0)
else :
  print(r-l)