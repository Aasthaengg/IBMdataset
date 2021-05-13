K, X = list(map(lambda n: int(n), input().split(" ")))
print(" ".join(list(map(lambda s: str(s), list(range(X - K + 1, X + K))))))