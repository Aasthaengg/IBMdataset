n,m = list(map(int, input().split()))
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]

for r in range(n-m+1):
    for c in range(n-m+1):
        flg=True
        for i in range(m):
            for j in range(m):
                if a[r+i][c+j] != b[i][j]:
                    flg=False
                    break
            if not flg:
                break
        if flg:
            print('Yes')
            exit()

print('No')