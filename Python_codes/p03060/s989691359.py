N=int(input())
V=[int(x) for x in input().split()]
C=[int(x) for x in input().split()]
ans=0
for v,c in zip(V,C):
    if v-c>0:
        ans+=v-c
print(ans)
