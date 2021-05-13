N,K = list(map(int,input().split()))
A = list(map(int,input().split()))
p = 10**9+7
Aplus = []
Nplus = 0
Aminus = []
Nminus = 0
Aabs = []
for i in range(N):
    if A[i]>=0:
        Aplus.append(A[i])
        Nplus += 1
    else:
        Aminus.append(A[i])
        Nminus += 1
Aplus.sort(reverse=True)
Aminus.sort(reverse=False)

if K==N:
    out=1
    for i in range(K):
        out = out*A[i]%p
    print(out)
elif Nminus==N and K%2==1:
    out=1
    for i in range(K):
        out = out*Aminus[N-i-1]%p
    print(out)
else:
    l=0
    r=0
    out=1
    inf = float('inf')
    while K>0:
        if l+1<=Nplus-1:
            cand1 = Aplus[l]*Aplus[l+1]
        elif l==Nplus-1:
            cand1 = Aplus[l]
        else:
            cand1 = -1*inf

        if r+1<=Nminus-1:
            cand2 = Aminus[r]*Aminus[r+1]
        elif r==Nminus-1:
            cand2 = Aminus[r]
        else:
            cand2 = -1*inf

        if cand1>cand2 or K==1:
            out=out*Aplus[l]%p
            K += -1
            l += 1
        else:
            out=out*Aminus[r]*Aminus[r+1]%p
            K += -2
            r += 2
    print(out)
