n = int(input())
s = list(input())

L = [0] * n
R = [0] * n

# 左にある W
for i in range(1, n):
    if s[i - 1] == 'W':
        L[i] = L[i - 1] + 1
    else:
        L[i] = L[i - 1]

# 右にある W
for i in range(n - 2, -1, -1):
    if s[i + 1] == 'E':
        R[i] = R[i + 1] + 1
    else:
        R[i] = R[i + 1]

res = 1 << 29
for i in range(n):
    res = min(res, L[i] + R[i])

print(res)