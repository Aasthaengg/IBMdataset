N, D = map(int, input().split())

A = D * 2 + 1

if N % A == 0:
    print(N // A)
else:
    print((N // A) + 1)