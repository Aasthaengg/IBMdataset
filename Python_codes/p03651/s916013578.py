import math

N,K = map(int,input().split())
A = list(map(int,input().split()))

if max(A) < K:
    print('IMPOSSIBLE')
else:
    check = A[0]
    for i in range(1,N):
        check = math.gcd(A[i],check)
    if K % check == 0:
        print("POSSIBLE")
    else:
        print('IMPOSSIBLE')