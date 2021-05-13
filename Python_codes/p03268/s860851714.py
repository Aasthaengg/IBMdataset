N, K = map(int, input().split())
A = N // K
if K % 2 != 0:
    print(A**3)
else:
    print(A**3 + ((N // (K//2)) - A)**3)