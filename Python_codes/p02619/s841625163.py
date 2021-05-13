D=int(input())
c=list(map(int,input().split()))
s=[list(map(int,input().split())) for _ in range(D)]
ld=[0]*26
ans=0
for i in range(D):
    v=int(input())-1
    ans+=s[i][v]
    ld[v]=i+1
    for j in range(26):
        ans-=(i+1-ld[j])*c[j]
    print(ans)