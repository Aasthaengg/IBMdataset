from collections import Counter
N=int(input())
s=[str(sorted(input())) for i in range(N)]

ans=0
cnt={}

for i in range(N):
    if s[i] in cnt:
        ans+=cnt[s[i]]
        cnt[s[i]]+=1
    else:
        cnt[s[i]]=1
        
print(ans)