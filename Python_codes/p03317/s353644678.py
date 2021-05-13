N, K = map(int, input().split())
A = list(map(int, input().split()))

g = 1

while N > K + (K - 1) * (g - 1):
    g += 1
print(g)
