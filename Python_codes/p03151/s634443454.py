n=int(input())
c=[]
d=[]
for a,b in zip(map(int,input().split()),map(int,input().split())):
  e=a-b
  if e<0:
    c.append(e)
  else:
    d.append(e)
if sum(c)+sum(d)<0:
  print(-1)
  exit()

cs=-sum(c)
d.sort(reverse=True)
sm=0
i=0
while sm<cs:
  sm+=d[i]
  i+=1
print(i+len(c))

