N,M=map(int,input().split())
li=[]
for i in range(M):
    a,b=map(int,input().split())
    li.append(a)
    li.append(b)
ans=[0]*N
for j in range(1,N+1):
    cj=li.count(j)
    ans[j-1]=cj
for k in range(N):
    print(ans[k])
