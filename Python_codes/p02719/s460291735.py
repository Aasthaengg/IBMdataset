N, K = map(int, input().split())

x = abs((N%K) - K)
if x > K/2:
    x = abs(x - K)
print(x)