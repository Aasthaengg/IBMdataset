import copy

h,w,k=map(int,input().split())
a=[]
for _ in range(h):
  b=list(input())
  a.append(b)

ans=0
for i in range(2**h):
  for j in range(2**w):
    c=copy.deepcopy(a)
    for x in range(h):
      if ((i>>x)&1):
        for u in range(w):
          c[x][u]='R'
          
    for y in range(w):
      if ((j>>y)&1):
        for t in range(h):
          c[t][y]='R'
    ch=0
    for z in c:
      ch+=z.count('#')
    if ch==k:
      ans+=1
      
print(ans)