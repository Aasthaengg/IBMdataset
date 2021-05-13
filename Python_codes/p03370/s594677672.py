N, X = map(int, input().split())
M = []
for _ in range(N):
    M.append(int(input()))
M.sort()
T = sum(M)
cnt = 0
while T + M[0] <= X:
    T+=M[0]
    cnt += 1
print(cnt + N)