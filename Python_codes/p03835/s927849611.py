k,s=map(int,input().split())
ans=0
for i in range(k+1):
    tmp=s-i
    if tmp<0:
        continue
    if tmp<=k:
        ans+=tmp+1
    elif 2*k<tmp:
        pass
    else:
        tmp1=2*k-tmp
        ans+=tmp1+1
    # print(tmp)
print(ans)