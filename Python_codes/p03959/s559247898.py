N = int(input())

T = list(map(int,input().split()))
A = list(map(int,input().split()))

X = [[T[0], 1]]
Y = [[A[N-1], 1]]

for i in range(1,N) :
    pv,pf = X[i-1]
    nv = T[i]
    
    if nv == 1 :
        X.append([nv, 1])
    elif pv >= nv :
        X.append([nv, 0])
    else :
        X.append([nv, 1])
    
    pv,pf = Y[i-1]
    nv = A[N-1-i]
    
    if nv == 1 :
        Y.append([nv, 1])
    elif pv >= nv :
        Y.append([nv, 0])
    else :
        Y.append([nv, 1])

Y = Y[::-1]

ans = 1

mat = 0
maa = 0

for i in range(N) :
    tv,tf = X[i]
    av,af = Y[i]
    
    mat = max(mat, tv)
    maa = max(maa, av)
    
    if tf == 1 and af == 0 :
        if tv > maa :
            ans = 0
            break
    elif tf == 0 and af == 1 :
        if av > mat :
            ans = 0
            break
    elif tf == 1 and af == 1 :
        if tv != av :
            ans = 0
            break
    else :
        ans *= min(tv,av)
        ans %= (10**9+7)
        
print(ans)
