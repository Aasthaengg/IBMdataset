N=int(input())
A = []
for _ in range(N):
    A.append(int(input()))

amax = max(A)
nmax = A.count(amax)
if nmax == 1:
    B = []
    for i in range(N):
        if A[i] != amax:
            B.append(A[i])
    asec = max(B)


for i in range(N):
    if A[i] == amax:
        if nmax > 1:
            ans = amax
        else:
            ans = asec
    else:
        ans = amax
    print(ans)