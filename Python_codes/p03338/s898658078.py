from collections import Counter
N=int(input())
S=input()

ans=0
l=Counter()
r=Counter(S)
for c in S:
    l[c]+=1
    r[c]-=1
    ans=max(ans,len(l&r))

print(ans)
