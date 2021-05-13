n,m=map(int,input().split())
A=list(map(int,input().split()))
R=[]
now=0
for i in range(n):
    now=(now+A[i])%m
    R.append(now)
R.sort()

cnt=1
now=0
Ans=[]
for i in range(n):
    if now==R[i]:
        cnt+=1
    else:
        if cnt>1:
            Ans.append(cnt)
        cnt=1
        now=R[i]
if cnt>1:
    Ans.append(cnt)
ans=0
for a in Ans:
    ans+=a*(a-1)//2
print(ans)