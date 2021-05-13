def getTheNumberOfCoin(n,m,C):
    T=[float('inf')]*(n+1)
    T[0]=0

    T=[float('inf')]*(n+1)
    T[0]=0
    for i in range(m):
        for j in range(C[i],n+1):
            T[j] = min(T[j], T[j - C[i]] + 1)
    return T[n]

n,m = map(int,raw_input().split())
C = map(int,raw_input().split())
print getTheNumberOfCoin(n,m,C)