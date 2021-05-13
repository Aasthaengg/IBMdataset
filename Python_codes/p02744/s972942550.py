from itertools import combinations
def g(i):
    return chr(i+96)
def f(n,i):
    global Ind
    if n==0:
        B.append("".join(A))
        return
    if n==1:
        j = Ind.pop()
        A[j] = g(i)
        B.append("".join(A))
        A[j]=0
        Ind.append(j)
        Ind = sorted(Ind)
        return
    j0 = Ind.pop(0)
    Ind1 = Ind[:]
    A[j0] = g(i)
    for k in range(n):
        for x in combinations(Ind1,n-1-k):
            tmp = []
            for j in range(n-1-k):
                A[x[j]] = g(i)
                tmp.append(x[j])
            for j in tmp:
                Ind.remove(j)
            f(k,i+1)
            for j in tmp:
                A[j] = 0
                Ind.append(j)
            Ind = sorted(Ind)
    Ind.append(j0)
    Ind = sorted(Ind)
    
N = int(input())
A = [0 for _ in range(N)]
Ind = list(range(N))
B = []
f(N,1)
B = sorted(B)
for b in B:
    print(b)