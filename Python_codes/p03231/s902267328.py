import fractions
N, M = map(int, input().split())
S = input()
T = input()

if N < M:
    N, M = M, N
    S, T = T, S

if N % M == 0:
    print(N if all([S[(N // M) * i] == T[i] for i in range(M)]) else -1)
    exit()
else:
    g = fractions.gcd(N, M)
    print(N // g * M if all([S[(N // g) * i] == T[(M // g) * i] for i in range(g)]) else -1)