H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
Ans = []
cnt = 0
for i in range(H):
    for j in range(W):
        if (i == H-1) and (j == W-1):
            continue
        if A[i][j] % 2 != 0:
            if j == W-1:
                A[i + 1][j] += 1
                Ans.append((str(i+1), str(j+1), str(i+2), str(j+1)))
            else:
                A[i][j + 1] += 1
                Ans.append((str(i+1), str(j+1), str(i+1), str(j+2)))

print(len(Ans))
for ans in Ans:
    print(' '.join(ans))

