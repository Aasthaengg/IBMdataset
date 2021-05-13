S=input()
N=len(S)

r=0
l=0
ans=[0]*N
i=0
while i<N:
    if S[i]=='R':
        if l>0:
            ans[i-l]=l
            x,y=i-l-1,i-l
            if ans[x]>ans[y]:
                if ans[x]%2:
                    ans[x],ans[y]=0--(ans[x]+ans[y])//2,(ans[x]+ans[y])//2
                else:
                    ans[x],ans[y]=(ans[x]+ans[y])//2,0--(ans[x]+ans[y])//2
            else:
                if ans[y]%2:
                    ans[x],ans[y]=(ans[x]+ans[y])//2,0--(ans[x]+ans[y])//2
                else:
                    ans[x],ans[y]=0--(ans[x]+ans[y])//2,(ans[x]+ans[y])//2

        r+=1
        l=0
    else:
        ans[i-1]=r
        r=0
        l+=1
    i+=1

ans[i-l]=l
x,y=i-l-1,i-l
if ans[x]>ans[y]:
    if ans[x]%2:
        ans[x],ans[y]=0--(ans[x]+ans[y])//2,(ans[x]+ans[y])//2
    else:
        ans[x],ans[y]=(ans[x]+ans[y])//2,0--(ans[x]+ans[y])//2
else:
    if ans[y]%2:
        ans[x],ans[y]=(ans[x]+ans[y])//2,0--(ans[x]+ans[y])//2
    else:
        ans[x],ans[y]=0--(ans[x]+ans[y])//2,(ans[x]+ans[y])//2

print(*ans)