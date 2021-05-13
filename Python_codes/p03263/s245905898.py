h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]

if h == 1 and w == 1:
    print(0)
    exit()

cnt = 0
ans = []
for i in range(h):
    for j in range(w):
        a = A[i][j]
        if a%2 == 1:
            for dy, dx in (-1, 0), (0, -1), (0, 1), (1, 0):
                ni = i+dy
                nj = j+dx
                if 0 <= ni < h and 0 <= nj < w:
                    ni_ = ni
                    nj_ = nj
                    if A[ni][nj]%2 == 1:
                        A[ni][nj] += 1
                        A[i][j] -= 1
                        cnt += 1
                        ans.append([i+1, j+1, ni+1, nj+1])
                        break
            else:
                A[ni_][nj_] += 1
                A[i][j] -= 1
                cnt += 1
                ans.append([i+1, j+1, ni_+1, nj_+1])

print(cnt)
for i in range(cnt):
    print(*ans[i])
