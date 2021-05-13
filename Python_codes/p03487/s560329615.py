from collections import Counter
N=int(input())
a=list(map(int,input().split()))

ans=0
cnt = Counter(a)
for k,v in cnt.items():
    if k>v:
        ans+=v
    else:
        ans+=v-k
print(ans)