N,C=map(int,input().split())
xv=[(0,0)]
xv_=[]
for i in range(N):
    x,v=map(int,input().split())
    xv.append((x,v))
    xv_.append((x,v))
xv_.append((C,0))
xv_.reverse()
r=[0]*(N+1)
r_=[0]*(N+1)
for i in range(N):
    r[i+1]=r[i]-(xv[i+1][0]-xv[i][0])+xv[i+1][1]
    r_[i+1]=max(r_[i],r[i+1]-xv[i+1][0])
l=[0]*(N+1)
l_=[0]*(N+1)
for i in range(N):
    l[i+1]=l[i]-abs(xv_[i+1][0]-xv_[i][0])+xv_[i+1][1]
    l_[i+1]=max(l_[i],l[i+1]-(C-xv_[i+1][0]))
ans=0
for i in range(1,N+1):
    ans=max(r[i]+l_[N-i],ans)
    ans=max(l[i]+r_[N-i],ans)
print(ans)
