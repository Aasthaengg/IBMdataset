from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))

ld=defaultdict(int)
rd=defaultdict(int)
for i in range(n):
    l=i+a[i]
    r=i-a[i]
    ld[l]+=1
    rd[r]+=1
ans=0
for i,j in ld.items():
    ans+=j*rd[i]

print(ans)
