N, M = map(int, input().split())

t = 1900 * M + 100 * (N - M)
A = 1 - (1/2) ** M
B = (1 - A) ** 2

print(int((1/2)**M * t / B))