
N = int(input())
X = list(map(int, input().split()))

y = [0] * (N + 1)
for i in reversed(range(1, N + 1)):
    cnt = 0
    for j in range(2 * i, N + 1, i):
        cnt += y[j]
    if cnt % 2 != X[i - 1]:
        y[i] = 1

print(sum(y))
if sum(y):
    print(*[i for i in range(N + 1) if y[i]])
