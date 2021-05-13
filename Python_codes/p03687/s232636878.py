s=input()

x=dict()
for i in range(len(s)):
    S=s[i]
    if S in x:
        x[S]+=1
    else:
        x[S]=1
M=0
cnt=0
for idx in x:
    M=max(M,x[idx])
    cnt+=1
if cnt==1:
    print(0)
    exit()
#y=sorted(x.items(),key=lambda x:x[1],reverse=True)
ans=10**10
#print(y)
for idy in x:
    t=s
    tmp=t
    count1=0
    count2=0
    cnt=0
    #print(idy)
    while(1):
        p=tmp
        tmp=""
        flag=True
        #print(p)
        for i in range(len(p)-1):
            if p[i]==idy or p[i+1]==idy:
                tmp=tmp+idy
                #count1+=1
                #print(tmp)
            else:
                tmp=tmp+p[i]
                #count2+=1
                flag=False
                #print(tmp)
        #print(tmp)
        cnt+=1
        if flag:
            break
    #cnt=count1+count2

    ans=min(cnt,ans)
print(ans)