n, k = list(map(int, input().split()))
mod = int(1e9 + 7)

q = [0] * (k + 1)
for i in range(1, k+1)[::-1]:
    q[i] = pow(k//i, n, mod)
    for j in range(2, k // i + 1):
        if i * j > k:
            continue
        q[i] -= q[i * j]
s = 0
for i, qq in enumerate(q):
    s += i * qq
    s %= mod
print(s)