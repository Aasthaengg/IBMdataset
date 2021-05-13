N,*B=map(int, open(0).read().split())
res=[]
while B:
    C=[i-b for i,b in enumerate(B,1)]
    if any(c<0 for c in C):
        print(-1)
        break
    D=[i for i,c in enumerate(C) if c==0]
    if D:
        res.append(D[-1]+1)
        B=B[:D[-1]]+B[D[-1]+1:]
    else:
        print(-1)
        break
else:
    print(*res[::-1], sep="\n")