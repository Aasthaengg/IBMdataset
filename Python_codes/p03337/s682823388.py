A, B = map(int, input().strip().split())

print(max(max(A + B, A - B), A * B))
