N,P = map(int,input().split())
A = list(map(int,input().split()))
C = [0,0]
for i in range(N):
    if A[i]%2==0:
        C[0] += 1
    else:
        C[1] += 1
if C[1]==0 and P==1:
    print(0)
elif C[1]==0 and P==0:
    print(2**C[0])
else:
    print((2**C[0])*(2**(C[1]-1)))