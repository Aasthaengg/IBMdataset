
n,k= map(int, input().split())
t= [list(map(int, input().split())) for i in range(n)]
q=[]
ans=0
r=[0]*(n+1)

t.sort(key=lambda x:x[1],reverse=True)

for i in range(k):
    ans += t[i][1]
    if r[t[i][0]]==0:
        r[t[i][0]]=1
    else:
        q.append(t[i][1])
v=sum(r)
ans+=v**2
cnt=ans


for i in range(k,n):
    if r[t[i][0]]==0 and len(q)!=0:
        r[t[i][0]]=1
        x=q.pop()
        cnt+=t[i][1]+2*v+1-x
        v+=1
        ans=max(cnt,ans)
print(ans)