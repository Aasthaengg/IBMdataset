#!/usr/bin/env python3
import fractions

def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

N, M = map(int, input().split())
S = input()
T = input()
if S[0] != T[0]:
    print(-1)
    exit()

l = lcm(N, M)

Moji = {}
Moji[0] = S[0]

for i in range(1, N):
    index = i * (l//N) + 1
    Moji[index-1] = S[i]

for i in range(1, M):
    index = i * (l//M) + 1
    if index-1 in Moji and Moji[index-1] != T[i]:
        print(-1)
        exit()

print(l)
