N,M,C = map(int,input().split())
B = list(map(int,input().split()))
A = [list(map(int,input().split())) for i in range(N)]
cnt = 0
for i in range(N):
    num = 0
    for j in range(M):
        num += A[i][j] * B[j]
    if num > -C:
        cnt += 1

print(cnt)