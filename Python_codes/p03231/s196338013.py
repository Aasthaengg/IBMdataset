import fractions

def lcm(a, b):
    return a * b / fractions.gcd(a, b)

N, M = map(int, input().split())
S = input()
T = input()

d_N = {}

for n in range(N):
    d = fractions.gcd(n, N)
    d_N[(n // d, N // d)] = n

for m in range(M):
    d = fractions.gcd(m, M)
    k = (m // d, M // d)
    if k in d_N:
        if S[d_N[k]] != T[m]:
            print(-1)
            exit()

L = int(lcm(N, M))
print(L)