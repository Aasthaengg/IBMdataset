import sys

K, A, B = map(int, sys.stdin.readline().split())

if K + 1 < A:
    print(K+1)
else:
    if A + 2 < B:
        # print("here")
        n = K - (A - 1)
        r = n // 2
        # print(n % 2)
        print(A + r * (B - A) + n % 2)
            
    else:
        print(K+1)