M,K = map(int,input().split())

def createL(k):
    L = []
    for i in range(2**M):
        if i!=k: L.append(i)
    return L,L[:][::-1]

S = []
if K>=(2**M):
    print(-1)
elif M==0:
    print("0 0")
elif M==1:
    if K==1: print(-1)
    else: print("0 0 1 1")
else:
    L,Lrev = createL(K)
    print(" ".join(str(i)for i in L+[K]+Lrev+[K]))