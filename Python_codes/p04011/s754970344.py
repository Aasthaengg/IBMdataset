N, K, X, Y = [int(input()) for _ in range(4)]

discounted_dates = N - K
if discounted_dates < 0:
    discounted_dates = 0

print((N * X) - (X - Y) * discounted_dates)