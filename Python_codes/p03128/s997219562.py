def check(i):
    global kmax,nmax
    cnt = 0
    for j in range(i):
        cnt += K[j]*B[j]
    if sum(B[:i])+(N-cnt)//K[i]<kmax:
        return
    for k in range((N-cnt)//K[i],-1,-1):
        if cnt+K[i]*k==N:
             if kmax<=sum(B[:i])+k:
                    kmax = sum(B[:i])+k
                    B[i] = k
                    num = ""
                    for j in range(len(K)):
                        num += str(D[j])*B[K.index(C[D[j]])]
                    num = int(num)
                    nmax = max(nmax,num)
        else:
            if i<len(K)-1:
                B[i] = k
                check(i+1)
            else:
                B[i] = 0
                return
C = {1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
N,M = map(int,input().split())
A = list(map(int,input().split()))
G = {}
for i in range(M):
    a = A[i]
    k = C[a]
    if k not in G:
        G[k] = 0
    if a>G[k]:
        G[k] = a
K = sorted(list(G.keys()))
D = sorted(list(G.values()),reverse=True)
B = [0 for _ in range(len(K))]
kmax = 0
nmax = 0
check(0)
print(nmax)