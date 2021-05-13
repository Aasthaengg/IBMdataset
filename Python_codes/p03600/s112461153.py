import sys
input = sys.stdin.readline

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
A2 = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        A2[i][j] = A[i][j]
for k in range(N):
    for i in range(N):
        for j in range(N):
            A2[i][j] = min(A2[i][j], A2[i][k]+A2[k][j])
ok = True
for i in range(N):
    for j in range(N):
        if A[i][j] != A2[i][j]:
            ok = False
if not ok:
    print(-1)
    exit()
ans = 0
for i in range(N):
    for j in range(N):
        connected = True
        for k in range(N):
            if i == k or j == k: continue
            if A[i][j] == A[i][k]+A[k][j]:
                connected = False
                break
        if connected:
            ans += A[i][j]
print(ans//2)
