from bisect import bisect as b

H,W=map(int,input().split())
S=[list(input()) for _ in range(H)]

X=[]
HL=[[] for _ in range(H)]
WL=[[] for _ in range(W)]
for h in range(H):
    for w in range(W):
        if S[h][w]=="#":
            HL[h].append(w)
            WL[w].append(h)

ans=0

for h in range(H):
    for w in range(W):
        if S[h][w]==".":
            if len(HL[h])==0:
                hol=W
            else:
                x=b(HL[h],w)
                N=len(HL[h])
                if x==0:
                    hol=HL[h][x]
                elif x==N:
                    hol=W-1-HL[h][-1]
                else:
                    hol=HL[h][x]-HL[h][x-1]-1

            if len(WL[w])==0:
                ver=H
            else:
                y=b(WL[w],h)
                M=len(WL[w])
                if y==0:
                    ver=WL[w][y]
                elif y==M:
                    ver=H-1-WL[w][-1]
                else:
                    ver=WL[w][y]-WL[w][y-1]-1
            ans=max(ans,ver+hol-1)
print(ans)