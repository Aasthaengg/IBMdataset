from fractions import gcd

N, M = map(int, input().split())

S = input()
T = input()

G = gcd(N, M)

n = N // G
m = M // G

L = N * M // G

for i in range(0, G):
    a = i * n
    b = i * m

    if S[a] != T[b]:
        print(-1)
        exit()

print(L)
