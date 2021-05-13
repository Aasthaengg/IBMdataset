n, k = map(int, input().split())
p = 10**9+7
F = {}
s = 0
for i in range(k, 0, -1):
    F[i] = pow(k//i, n, p)
    for j in range(2*i, k+1, i):
        F[i] -= F[j]
    s = (s + F[i] * i) % p
print(s)