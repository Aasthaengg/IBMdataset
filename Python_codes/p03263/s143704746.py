h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]

cnt = 0
X = []
for i in range(h):
    for j in range(w):
        if A[i][j]%2 ==1:
            if j != w-1:
                cnt += 1
                X.append((i+1, j+1, i+1, j+2))
                A[i][j+1] += 1
            else:
                if i != h-1:
                    cnt += 1
                    X.append((i+1, j+1, i+2, j+1))
                    A[i+1][j] += 1
print(cnt)
for x in X:
    print(*x)
