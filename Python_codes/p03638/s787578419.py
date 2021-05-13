H, W = map(int,input().split())
N = int(input())
A = list(map(int,input().split()))
for i in range(N-1):
    A[i+1] = A[i] + A[i+1]
C = [[0 for i in range(W)] for j in range(H)]
cnt = 1
index = 0
for i in range(H):
    for j in range(W):
        if cnt > A[index]:
            index += 1
        C[i][j] = index + 1
        cnt += 1
for i in range(H):
    if i % 2 == 0:
        print(*C[i])
    else:
        print(*C[i][::-1])