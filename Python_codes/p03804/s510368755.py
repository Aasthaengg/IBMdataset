n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]

ans = 'No'
for x in range(0, n - m + 1):
    for y in range(0, n - m + 1):
        check = True
        for i in range(m):
            for j in range(m):
                if a[i+x][j+y] != b[i][j]:
                    check = False
                    break
            if check == False:
                break
        if check == True:
            ans = 'Yes'
            break
print(ans)
