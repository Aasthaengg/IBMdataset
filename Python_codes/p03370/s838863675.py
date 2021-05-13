N, X = map(int, input().split())
M = []
for i in range(N):
    m = int(input())
    M.append(m)
print(N + (X - sum(M)) // min(M))
