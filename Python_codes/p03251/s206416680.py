N,M,X,Y=map(int,input().split())
XL=sorted(list(map(int,input().split())))
YL=sorted(list(map(int,input().split())))
ans = 'War'

for Z in range(X+1,Y+1):
    if XL[-1]<Z and Z<=YL[0]:
        ans = 'No War'
        break

print(ans)