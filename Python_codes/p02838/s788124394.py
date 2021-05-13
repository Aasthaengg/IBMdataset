N = int(input())
A = list(map(int, input().split()))
L = 60
MOD = 10**9 + 7
data = [0]*L
for a in A:
    S = reversed(bin(a)[2:])
    for i, s in enumerate(S):
        data[i] += s=="1"
p = 1
res = 0
for i in range(L):
    res += data[i]*(N-data[i])*p
    p *= 2
    p %= MOD
print(res%MOD)