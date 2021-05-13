import fractions

N, K = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
A.sort()
diff = 10 ** 9

if max(A) < K:
    print('IMPOSSIBLE')
else:
    gcd = max(A)
    for i in range(N):
        gcd = fractions.gcd(gcd, A[i])

    if K % gcd == 0:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')