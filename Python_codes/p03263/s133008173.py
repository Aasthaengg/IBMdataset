
def resolve():
    h, w  = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = []
    for i in range(h):
        for j in range(w):
            if j != w-1 :
                if a[i][j] % 2 == 0:
                    continue
                else:
                    ans.append([i+1, j+1, i+1, j+2])
                    a[i][j+1] += 1
                    a[i][j] -= 1
    for i in range(h):
        if i != h-1:
            if a[i][w-1] % 2 == 0:
                continue
            else:
                ans.append([i+1, j+1, i+2, j+1])
                a[i+1][w-1] += 1
                a[i][w-1] -= 1
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])
resolve()