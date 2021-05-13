N,M= map(int,input().split())
l=list(map(int,input().split()))
tmp=[]
for i in l:
   tmp.append((1,i))
for i in range(M):
   A,B=list(map(int,input().split()))
   tmp.append((A,B))
from operator import itemgetter
tmp.sort(reverse=True,key=itemgetter(1))
ans,cnt=0,N
for v,s in tmp:
   nd=min(v,cnt)
   ans+=nd*s
   cnt-=nd
print(ans)