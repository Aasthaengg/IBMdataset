N,K = map(int,input().split())
A = sorted([list(map(int,input().split())) for _ in range(N)],key=lambda x:x[1],reverse=True)
C = {}
tot1 = 0
for i in range(K):
    t,d = A[i]
    if t not in C:
        C[t] = 0
    C[t] += 1
    tot1 += d
tot2 = len(C)
tot = tot1+tot2**2
cur = K
for i in range(K-1,-1,-1):
    t,d = A[i]
    if C[t]>1:
        tot1 -= d
        C[t] -= 1
        j = cur
        while j<N:
            t1,d1 = A[j]
            if t1 not in C:
                C[t1]=1
                tot1 += d1
                tot2 += 1
                if tot1+tot2**2>tot:
                    tot = tot1+tot2**2
                cur = j+1
                break
            else:
                j += 1
                cur = j
print(tot)