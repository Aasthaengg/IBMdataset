N, M = map(int, input().split())
if N >= 2 and M >= 2:
    print(N*M - (2*(N+M)-4))
elif N == 1 and M == 1:
    print(1)
else:
    print(N*M-2)