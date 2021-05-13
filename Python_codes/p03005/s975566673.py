def inpl():
    return list(map(int, input().split()))


N, K = inpl()
print(N - K if K > 1 else 0)