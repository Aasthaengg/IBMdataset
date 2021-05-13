N, K, X, Y = [int(input()) for i in range(4)]
res = 0
for i in range(N):
    if i < K:
        res += X
    else:
        res += Y
print(res)