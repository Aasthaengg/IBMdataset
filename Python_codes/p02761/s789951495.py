N,M=map(int,input().split())
li=["&"]*N
a=True
for i in range(M):
    s,c=map(int,input().split())
    if s==1 and c==0 and N!=1:
        ans="-1"
        a=False
    else:
        if li[s-1]=="&":
            li[s-1]=c
        else:
            if li[s-1]==c:
                pass
            else:
                ans="-1"
                a=False
if a==True:
    ans=""
    for j in range(N):
        if li[j]=="&" and j!=0:
            li[j]=0
        elif li[j]=="&" and j==0 and N!=1:
            li[j]=1
        elif li[j]=="&" and j==0 and N==1:
            li[j]=0
        ans+=str(li[j])
print(ans)

