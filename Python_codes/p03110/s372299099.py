N=int(input())
xy=[list(input().split())for _ in range(N)]

ans=0
for x,y in xy:
    if y=='JPY':
        ans+=int(x)
    else:
        ans+=float(x)*380000

print(ans)