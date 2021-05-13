H, W = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(H)]

tmp = 0

ans = []

for j in range(H):
    if j % 2 == 0:
        for i in range(W):
            if j == H-1 and i == W-1:
                break
            if A[j][i] % 2 != 0:
                A[j][i] -= 1
                if i == W-1:
                    A[j+1][i] += 1
                    ans.append([j, i, j+1, i])
                else:
                    A[j][i+1] += 1
                    ans.append([j, i, j, i+1])

    else:
        for i in range(W-1, -1, -1):
            if j == H-1 and i == 0:
                break
            if A[j][i] % 2 != 0:
                A[j][i] -= 1
                if i == 0:
                    A[j+1][i] += 1
                    ans.append([j, i, j+1, i])
                else:
                    A[j][i-1] += 1
                    ans.append([j, i, j, i-1])


print(len(ans))
for a in ans:
    a[0] += 1
    a[1] += 1
    a[2] += 1
    a[3] += 1
    print(*a)
