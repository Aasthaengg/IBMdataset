n= int(input())
d = list(map(int,input().split()))
d.sort()
x=int(n/2)
if d[x] == d[x-1]:
  print(0)
else:
  y = d[x] - d[x-1]
  print(y)