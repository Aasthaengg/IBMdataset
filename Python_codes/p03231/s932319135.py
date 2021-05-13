from fractions import gcd

N, M = map(int, input().split())
S = input()
T = input()


def lcm(n, m):
    return n // gcd(n, m) * m


n = N // gcd(N, M)
m = M // gcd(N, M)

for i in range(gcd(N, M)):
    if S[i * n] != T[i * m]:
        print("-1")
        break
else:
    print(lcm(N, M))
