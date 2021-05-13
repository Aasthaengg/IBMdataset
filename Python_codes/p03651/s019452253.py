from math import gcd
N,K = list(map(int,input().split()))
A = list(map(int,input().split()))

l = A[0]
for i in range(1,N):
    l = gcd(l,A[i])

m = max(A)
if m < K:
    print('IMPOSSIBLE')
else:
    if l == 1:
        print('POSSIBLE')
    else:
        for i in range(N):
            if abs(A[i]-K)%l == 0:
                print('POSSIBLE')
                break
        else:
            print('IMPOSSIBLE')
