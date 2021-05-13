N, M = map(int, input().split())

time = (M * 1900 + (N-M) * 100) / (0.5 ** M)
print(int(time))