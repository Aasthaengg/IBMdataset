import math
a,b=map(int,input().split())
List=[list(map(int,input().split())) for i in range(a)]
ans=10000000000000
for i in range(2**a):
  s=0
  c=0
  t=True
  x=0
  y=0
  for j in range(a):
    if (i>>j) & 1:
      s+=(a-j)*100*List[a-1-j][0]+List[a-1-j][1]
      c+=List[a-1-j][0]
    else:
      if t:
        x=(a-j)*100
        y=List[a-1-j][0]
        t=False
  if b<=s:
    if ans>c:
      ans=c
  else:
    if math.ceil((b-s)/x)<=y:
      c+=math.ceil((b-s)/x)
      if ans>c:
        ans=c
print(ans)