from collections import defaultdict
N=int(input())
D=defaultdict(int)
for i in range(N):
    a=int(input())
    D[a]+=1

ans=0
for v in D.values():
    if v%2==1:
        ans+=1

print(ans)