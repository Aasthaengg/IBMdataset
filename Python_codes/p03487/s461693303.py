from collections import Counter

n,*a=map(int,open(0).read().split())

cnt=Counter(a)

ans=0

for k,v in cnt.items():
    if v>=k:
        ans+=min(v-k,v)
    else:
        ans+=v

print(ans)