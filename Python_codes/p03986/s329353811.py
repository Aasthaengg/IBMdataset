x=input()
cnt=0
ans=0
for s in x:
    if s=="T":
        cnt-=1
    else:
        cnt+=1
    if cnt<0:
        ans+=1
        cnt=0
print(ans+cnt)