from itertools import combinations

N=int(input())
d=list(map(int,input().split()))

c=list(combinations(d,2))

ans=0

for i in range(len(c)):
    a=c[i][0]*c[i][1]
    ans+=a

print(ans)
