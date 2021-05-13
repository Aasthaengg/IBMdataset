N, X, T = [int(v) for v in input().rstrip().split()]
num = int((N + (X - 1)) / X)
r = T * num
print(r)
