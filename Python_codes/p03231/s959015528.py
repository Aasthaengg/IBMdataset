import math
N, M = map(int, input().split())
S = input()
T = input()
g = math.gcd(N,M)
print(N*M//g if S[::N//g] == T[::M//g] else -1)
