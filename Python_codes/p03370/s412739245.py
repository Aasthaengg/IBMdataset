def actual(N, X, M):
    rest_elements = X - sum(M)

    return N + (rest_elements // min(M))

N, X = map(int, input().split())
M = [int(input()) for _ in range(N)]

print(actual(N, X, M))