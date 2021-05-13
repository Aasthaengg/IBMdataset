N, X = map(int, input().split())
M = []
for i in range(N):
    M.append(int(input()))

r = X - sum(M)
min_resource = min(M)
q = r // min_resource

print(N + q)