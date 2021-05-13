N,P = map(int,input().split())
A = list(map(int,input().split()))
C = {0:0,1:0}
for i in range(N):
    if A[i]%2==0:
        C[0] += 1
    else:
        C[1] += 1
if P==0:
    if C[1]==0:
        n = 2**C[0]
    else:
        n = 2**C[0]*2**(C[1]-1)
else:
    if C[1]==0:
        n = 0
    else:
        n = 2**C[0]*2**(C[1]-1)
print(n)