from collections import Counter
N = int(input())
S = input()
MOD = 10**9 + 7

A = [0]*26
for e in S:
    A[ord(e)-97] += 1

ans = 1
for e in A:
    ans *= e+1
    ans %= MOD
print((ans-1)%MOD)
