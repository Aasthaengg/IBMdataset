N,M=list(map(int,input().split()))
l=[0]*N
for i in range(M):
   a,b=map(int,input().split())
   a-=1;b-=1
   l[a]+=1
   l[b]+=1
l=[i for i in l if i%2!=0]
print("YES") if len(l)==0 else print("NO")