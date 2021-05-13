N,P = map(int,input().split())
A = list(map(int,input().split()))
n0=0
n1=0
for i in range(N):
    if A[i]%2==0:
        n0 += 1
n1 = N-n0
if P==0:
    if n1==0:
        print(2**n0)
    else:
        print(2**(n1-1)*2**n0)
else:
    if n1==0:
        print(0)
    else:
        print(2**(n1-1)*2**n0)