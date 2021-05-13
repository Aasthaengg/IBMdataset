N, R = list(map(int, input().rstrip().split()))
D = R
if N < 10:
    v = 100 * (10 - N)
    # R = X - v
    D = R + v

print(D)

