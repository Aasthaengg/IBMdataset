H,W=map(int,input().split())
S=[input() for _ in range(H)]

D=[(0,1),(0,-1),(1,0),(-1,0)]

ans=True
for h in range(H):
    for w in range(W):
        if (S[h][w]=='#'):
            f=False
            for dh,dw in D:
                h2=h+dh
                w2=w+dw
                if h2<0 or H<=h2 or w2<0 or W<=w2: continue
                if S[h2][w2]=='#':
                    f=True
                    break
            else:
                ans=False
print('Yes' if ans else 'No')