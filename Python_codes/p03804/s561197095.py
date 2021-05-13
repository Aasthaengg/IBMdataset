n, m = map(int, input().split())

a = [list(map(str, input().rstrip())) for x in range(n)]
b = [list(map(str, input().rstrip())) for x in range(m)]

ans = []
for i in range(n - m + 1):
    for j in range(n - m + 1):
        tmp = []
        for x in range(m):
            for y in range(m):
                if a[i + x][j + y] == b[x][y]:
                    tmp.append(True)
                else:
                    tmp.append(False)
        ans.append(all(tmp))

print("Yes" if any(ans) else "No")