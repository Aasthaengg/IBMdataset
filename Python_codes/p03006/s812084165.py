from collections import Counter
n= int(input())
if n==1:
  print(1)
  exit()
xy=[[int(x) for x in input().split()] for _ in range(n)]
gr = [[[0,0]for _ in range(n)]for _ in range(n)]
for i in range(n):
  a,b = xy[i]
  for j in range(n):
    gr[i][j] = [xy[j][0]-a,xy[j][1]-b]
gr1 = []
for i in gr:
  for j in i:
    gr1.append(tuple(j))
#print(gr1)
c = Counter(gr1)
l,f = c.most_common()[0]
if l!=(0,0):
  print(n-f)
else:
  l,f = c.most_common()[1]
  print(n-f)