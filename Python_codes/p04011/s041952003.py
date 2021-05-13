n = 4
total = int(0)
zenhan = int(0)
kouhan = int(0)

N, K, X, Y = [int(input()) for i in range(4) ]

kouhan = (N - K ) * Y

if (N > K):
    zenhan = K * X
    total = zenhan + kouhan
else:
    zenhan = N * X
    total = zenhan

print(total)