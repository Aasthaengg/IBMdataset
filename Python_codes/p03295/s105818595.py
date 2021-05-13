a,b=map(int,input().split())
List=[]
for i in range(b):
  p,q=map(int,input().split())
  List.append([p,q])
List=sorted(List,key=lambda x:x[1])
ans=0
l=1
for i in range(b):
  if List[i][0]>=l:
    ans+=1
    l=List[i][1]
print(ans)