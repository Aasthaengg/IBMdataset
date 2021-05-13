n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]

d = n - m + 1
flg = False
for i in range(d):
    for j in range(d):
        if a[i][j : j + m] == b[0]:
            for k in range(1, m):
                if a[i + k][j : j + m] != b[k]:
                    break
            else:
                print("Yes")
                flg = True
                break
    if flg:
        break
else:
    print("No")