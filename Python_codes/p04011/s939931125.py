def actual(N, K, X, Y):
    if N <= K:
        return X * N

    return (X * K) + (Y * (N - K))

N = int(input())
K = int(input())
X = int(input())
Y = int(input())

print(actual(N, K, X, Y))
