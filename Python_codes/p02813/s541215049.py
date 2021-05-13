def getN(P,i):
    n=0
    P1=sorted(P)
    for p in range(i-1):
        n *=(i-p)
        n += (P1.index(P[p]))
        P1.remove(P[p])
    return n

n = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))

p = getN(P,n)
q = getN(Q,n)

print(abs(p-q))