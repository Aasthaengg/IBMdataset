def agc032_b():
    n = int(input())
    g = [[1]*n for _ in range(n)]
    for i in range(n//2):
        j = 2*(n//2)-1-i
        g[i][j] = 0
        g[j][i] = 0
    cnt = (sum([sum(row) for row in g]) - n) // 2
    print(cnt)
    for i in range(n):
        for j in range(i+1, n):
            if g[i][j]: print('{} {}'.format(i+1, j+1))

if __name__ == '__main__':
    agc032_b()