N,T=list(map(int,input().split()))
l=list(map(int,input().split()))
a_l=[]
ans=0
for i in range(N-1):
   a_l.append(l[i+1]-l[i])
for i in range(N-1):
   ans+=min(T,a_l[i])
ans+=T
print(ans)