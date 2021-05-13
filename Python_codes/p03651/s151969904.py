def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a

N,K = (int(x) for x in input().split())
A = list(map(int, input().split()))
m = max(A)
if N == 1:
    if A[0] == K:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')
else:
    if K > m:
        print('IMPOSSIBLE')
    else:
        gcd = xgcd(A[0],A[1])
        for i in range(2,N):
            gcd = xgcd(gcd,A[i])
            if gcd == 1:
                print('POSSIBLE')
                break
        else:
            if K % gcd == 0:
                print('POSSIBLE')
            else:
                print('IMPOSSIBLE')