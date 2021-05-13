N, K = map(int, input().split())
a = min(N%K, K-N%K)
print(a)
