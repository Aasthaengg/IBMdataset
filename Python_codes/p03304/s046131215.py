N, M, D = map(int, input().split())
print("{:.9f}".format((N-D)*(2 if D else 1)/(N*N)*(M-1)))