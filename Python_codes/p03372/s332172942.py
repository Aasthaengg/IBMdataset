n,c=map(int, input().split())
lst = [list(map(int, input().split())) for i in range(n)] 
ans=0
lback=[0]
rback=[0]
l=0
r=0
for i, j in enumerate(lst,1):
  l+=j[1]
  if(lback[i-1]<l-2*j[0]):
    lback+=[l-2*j[0]]
  else:
    lback+=[lback[i-1]]
  ans=max(ans,l-j[0])
for i, j in enumerate(lst[::-1],1):
  r+=j[1]
  if(rback[i-1]<r-2*(c-j[0])):
    rback+=[r-2*(c-j[0])]
  else:
    rback+=[rback[i-1]]
  ans=max(ans,r-(c-j[0]), lback[n-i]+r-(c-j[0]) )
l=0
for i, j in enumerate(lst,1):
  l+=j[1]
  ans=max(ans,rback[n-i]+l-j[0])
print(ans)