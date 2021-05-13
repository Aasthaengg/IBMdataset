def actual(D, N):
    if N == 100:
        return (100 ** D) * N + (100 ** D)

    return (100 ** D) * N

D, N = map(int, input().split())
print(actual(D, N))