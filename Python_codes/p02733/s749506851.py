H,W,K=map(int,input().split())
S=[list(map(int,list(input()))) for i in range(H)]
ans=H+W-2
for bit in range(2**(H-1)):
    divH=[0]
    for j in range(H-1):
        if(bit>>j&1):
            divH.append(j+1)
    divH.append(H)
    glen=len(divH)-1
    group=[0]*(glen)
    res=glen-1
    go=True
    for w in range(W):
        ok=True
        c=[0]*(glen)
        for g in range(glen):
            cum=0
            for h in range(divH[g],divH[g+1]):
                cum+=S[h][w]
            c[g]+=cum
            if cum>K:
                go=False
            if cum+group[g]>K:
                ok=False
        if not go:
            break
        if not ok:
            res+=1
            group=[c[i] for i in range(glen)]
        else:
            for i in range(glen):
                group[i]+=c[i]
    if not go:
        continue
    ans=min(ans,res)
print(ans)
