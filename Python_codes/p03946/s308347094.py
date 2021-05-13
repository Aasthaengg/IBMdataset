
N,T = map(int,input().split())

A = list(map(int,input().split()))

nmin = float("inf")
nsub = 0
ans = 0

Acopy = A.copy()
Acopy.sort()

for i in Acopy:

    if A[-1] == i:
        del A[-1]
    else:
        break


for i in range(len(A)):

    nmin = min(nmin , A[i])

    if nsub < A[i] - nmin:
        nsub = A[i] - nmin
        ans = 1

    elif nsub == A[i] - nmin:
        ans += 1

print (ans)
