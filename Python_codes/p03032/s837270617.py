N,K =map(int, input().split())
V=list(map(int, input().split()))
res=0
for l in range(K+1):
    for r in range(K+1-l):
        if l+r>N: continue
        t=V[:l]+V[N-r:]
        t.sort()
        S=sum(t)
        for c in range(min(K-l-r,l+r)):
            if t[c]<0:
                S-=t[c]
        res=max(res,S)
print(res)