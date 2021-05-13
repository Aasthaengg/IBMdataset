
N = int(input())
X = list(map(int, input().split()))

b = [0] * N
res = 0
for i in range(N):
    res += X[i] * (-1) ** i
b[0] = res // 2

for i in range(1, N):
    b[i] = X[i - 1] - b[i - 1]

print(*[v * 2 for v in b])
