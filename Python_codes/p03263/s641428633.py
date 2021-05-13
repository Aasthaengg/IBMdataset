H, W = map(int, input().split())
K = []
for i in range(H):
    A = list(map(int, input().split()))
    K.append(A)

Ans = []
i = 0
while(True):
    for j in range(W-1):

        if K[i][j]%2 == 1:
            K[i][j] -= 1
            K[i][j+1] += 1
            Ans.append((i+1, j+1, i+1, j+2))
    i += 1
    if i >= H:
        break
    if K[i-1][W-1] % 2 == 1:
        K[i-1][W-1] -= 1
        K[i][W-1] +=1
        Ans.append((i, W, i+1, W))
    for j in range(W-1, 0, -1):
        if K[i][j]%2 == 1:
            K[i][j] -= 1
            K[i][j-1] += 1
            Ans.append((i+1, j+1, i+1, j))
    i += 1
    if i >= H:
        break
    if K[i-1][0] % 2 == 1:
        K[i-1][0] -= 1
        K[i][0] += 1
        Ans.append((i, 1, i+1, 1))

print(len(Ans))
for i in Ans:
    print(*i)