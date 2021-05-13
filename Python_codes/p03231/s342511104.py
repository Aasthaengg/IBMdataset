from math import gcd

N, M = map(int, input().split())
S = input()
T = input()

L = N*M // gcd(N, M)

for i in range(N):
    if M*i % N == 0:
        j = M*i // N
        if S[i] != T[j]:
            print(-1)
            exit()

print(L)
