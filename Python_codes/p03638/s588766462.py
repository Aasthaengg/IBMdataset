
H,W = map(int, input().split())
N= int(input())
A = list(map(int, input().split()))


ans = [[0 for _ in range(W)] for _ in range(H)]


cnt = 0
c = 0
for i in range(H):
    if i % 2 == 0:
        for j in range(W):
            ans[i][j] = c+1
            A[c] -= 1
            if A[c] == 0:
                c += 1
    else:
        for j in reversed(range(W)):
            ans[i][j] = c+1
            A[c] -= 1
            if A[c] == 0:
                c += 1

for i in range(H):
    print(*ans[i])