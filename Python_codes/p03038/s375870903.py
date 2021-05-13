n,m=map(int,input().split())
a=[0]*n
List={}
a=list(map(int,input().split()))
for i in range(n):
  List.setdefault(a[i],0)
  List[a[i]]+=1
ans=0

for i in range(m):
  b,c=map(int,input().split())
  List.setdefault(c,0)
  List[c]+=b
  
List_sorted=sorted(List, reverse=True)

#print(List)
#print(List_sorted)
for i in List_sorted:
  if (List[i]<n):
    ans+=i*List[i]
    n-=List[i]
  else:
    ans+=i*n
    break
    
print(ans)