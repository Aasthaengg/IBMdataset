N, A, B = map(int, input().split())
m = min(A, B)
M = max(A + B - N, 0)

print(m, M)
