N, M = sorted(map(int, input().split()))
if N == M == 1:
    print(1)
elif N == 1:
    print(M-2)
else:
    print((N-2)*(M-2))