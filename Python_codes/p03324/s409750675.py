D, N = map(int, input().split())
print([100 ** D * i for i in range(102) if i%100 != 0][N-1])