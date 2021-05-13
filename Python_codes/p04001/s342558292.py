S=input()
n=len(S)-1
ans=0
for i in range(2**n):
    tmp=S
    cnt=0
    for j in range(n):
        if (i>>j)&1:
            tmp=tmp[:j+1+cnt]+" "+tmp[j+1+cnt:]
            cnt+=1
    ans+=sum(list(map(int,tmp.split(" "))))
print(ans)