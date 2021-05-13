N, K, X, Y = [int(input()) for i in range(4)]

#print("{} {} {} {}".format(N, K, X, Y))

res = 0

for i in range(N):
    if i + 1 <= K:
        res += X
    else:
        res += Y

print(res)
