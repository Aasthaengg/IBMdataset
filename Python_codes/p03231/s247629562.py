from fractions import gcd

N, M = map(int, input().split())
S = input()
T = input()

lcm = N * M // gcd(N, M)
n = N // gcd(N, M)
m = M // gcd(N, M)

for k in range(gcd(N, M)):
    a = k * n
    b = k * m
    if S[a] != T[b]:
        print(-1)
        exit()

print(lcm)
