N = int(input())

if N%2==1:
    L = [[N]]
    for i in range(1,N//2+1):
        L.append([i,N-i])
else:
    L = []
    for i in range(1,N//2+1):
        L.append([i,N-i+1])
LN = len(L)
M = []
for i in range(LN):
    A = L[i]
    for j in range(i+1,LN):
        B = L[j]
        for Ai in A:
            for Bi in B:
                M.append([Ai,Bi])

MN = len(M)
print(MN)
for i in range(MN):
    print(M[i][0],M[i][1])