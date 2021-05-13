D, G = map(int,input().split())
p,C = [],[]
for i in range(D):
    p_,c_ = map(int,input().split())
    p.append(p_)
    C.append(c_)
ans = float('inf')
 
for i in range(2**D):
    s, k = 0, 0
 
    for j in range(D):
        if (i>>j) & 1:
            s += p[j]*(j+1)*100 + C[j] 
            k += p[j]
    if s >= G:
        ans = min(ans, k)
    else:
        for l in range(D-1, -1, -1):
            if (i>>l) & 1 == 0: 
                if s+(l+1)*100*p[l]<G:
                    break
                else:
                    rem = G - s
                    k += -(-rem//((l+1)*100))
                    ans = min(ans, k)
print(ans)
