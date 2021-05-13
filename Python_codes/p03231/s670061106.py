import fractions
N,M = [int(hoge) for hoge in input().split()]
S = input()
T = input()
G = fractions.gcd(N,M)
print(N*M//G) if S[::N//G] == T[::M//G] else print(-1)