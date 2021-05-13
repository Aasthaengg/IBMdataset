n, m = map(int, input().split())
a, b = [], []
for _ in range(n):
    a.append(input())
for _ in range(m):
    b.append(input())

# (i, j)ずらす
for i in range(n-m+1):
    for j in range(n-m+1):
        flag = True
        for x in range(m):
            for y in range(m):
                if b[x][y] != a[x+i][y+j]:
                    break
            else:
                continue
            flag = False
            break
        if flag:
            print('Yes')
            exit()

print('No')