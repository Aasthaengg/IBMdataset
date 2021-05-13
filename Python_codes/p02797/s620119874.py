N, K, S = map(int, input().split())
l = [S]*K+[(S+1)%(10**9)]*(N-K)
print(' '.join(map(str, l)))