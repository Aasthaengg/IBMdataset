n,m=map(int,input().split())
lst=[list(map(int,input().split())) for i in range(m)]

x=[]
y=[]

for i in lst:
  if i[0]==1:
    x+=[i[1]]
    
for i in lst:
  if i[1]==n:
    y+=[i[0]]
    
ans='POSSIBLE'

if len(list(set(x)))+len(list(set(y)))==len(list(set(x+y))):
  ans='IMPOSSIBLE'
    
print(ans)
