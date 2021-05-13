import sys
N=int(input())
ans,c=0,{}
for _ in range(N):
    s=''.join(sorted(next(sys.stdin)))
    if s not in c:
         c[s]=0
    ans+=c[s]
    c[s]+=1
print(ans)
