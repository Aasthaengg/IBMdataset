N, D = list(map(int, input().rstrip().split()))
cover = D * 2 + 1
result = int((N + cover - 1) / cover)
print(result)
