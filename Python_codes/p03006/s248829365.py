from collections import defaultdict
n=int(input())
xy=[list(map(int,input().split())) for _ in range(n)]
if n==1:
  print(1)
  exit()
d=defaultdict(lambda:0)
for i in range(n-1):
  for j in range(i+1,n):
    dx=xy[i][0]-xy[j][0]
    dy=xy[i][1]-xy[j][1]
    d[(dx,dy)]+=1
    d[(-dx,-dy)]+=1
print(n-max(d.values()))
#for k,v in d.items():
#  print(k,v)
