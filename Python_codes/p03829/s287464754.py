N, A, B = map(int, input().split())
X = list(map(int, input().split()))
num = 0
for i in range(N - 1):
    diff = X[i + 1] - X[i]
    num += min(diff * A, B)
print(num)
