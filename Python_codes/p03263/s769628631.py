h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]

ans = []
for i in range(h):
    for j in range(w):
        if A[i][j]%2 == 1:
            if j != w-1:
                A[i][j+1] += 1
                ans.append((i+1, j+1, i+1, j+2))
            else:
                if i != h-1:
                    A[i+1][j] += 1
                    ans.append((i+1, j+1, i+2, j+1))
print(len(ans))
for i in range(len(ans)):
    print(*ans[i])
