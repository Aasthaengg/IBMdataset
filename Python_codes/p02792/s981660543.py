n = int(input())

check = [[0] * 9 for i in range(9)]

if n <= 10:
    print(n)
else:
    for i in range(1, n+1):
        I = str(i)
        if I[-1] != '0':
            check[int(I[0]) - 1][int(I[-1]) - 1] += 1
    ans = 0
    for i in range(9):
        for j in range(9):
            ans += check[i][j] * check[j][i]
    print(ans)