N, C, K = map(int, input().split())

T = sorted([int(input()) for _ in range(N)])

x = T[0]
p = 1
b = 1
for i in range(1, N):
    if T[i] <= x + K and p < C:
        p += 1
    else:
        x = T[i]
        b += 1
        p = 1
print(b)