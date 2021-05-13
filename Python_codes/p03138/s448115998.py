N, K = map(int, input().split())
A = list(map(int, input().split()))

L = [0] * 50

for a in A:
    i = 0
    while a > 0:
        L[i] += a & 1
        i += 1
        a >>= 1

X = 0
ans = 0
for i in range(49, -1, -1):
    if L[i] < (N + 2 - 1) // 2 and X + (1 << i) <= K:
        num = N - L[i]
        bit = 1
    else:
        num = L[i]
        bit = 0
    ans += (1 << i) * num
    X += (bit << i)

print(ans)
