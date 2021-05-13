mod=10**9+7

H,W=map(int,input().split())
a=[list(input()) for _ in range(H)]
a[0][0]=1
for h in range(H):
    for w in range(W):
        if h==0:
            if w==0:
                continue
            if a[h][w]==".":
                a[h][w]=a[h][w-1]
            else:
                a[h][w]=0
        else:
            if a[h][w]=="#":
                a[h][w]=0
            elif w==0:
                a[h][w]=a[h-1][w]
            else:
                a[h][w]=(a[h-1][w]+a[h][w-1])%mod
print(a[-1][-1])