N, M = map(int, input().split())
case = 2 ** M
time = 100 * (N-M) + 1900 * M
X = case * time
print(X)