def solve():
    n, m = map(int, input().split())
    d = [{} for _ in range(n)]
    ans = [0 for _ in range(m)]
    for i in range(m):
        p, y = map(int, input().split())
        d[p-1][i] = y
    for i in range(n):
        d[i] = sorted(d[i].items(), key=lambda x:x[1])
        d[i] = list(map(list, d[i]))
        for x in range(len(d[i])):
            ans[d[i][x][0]] = '{:0=6}'.format(i + 1) + '{:0=6}'.format(x + 1)
    for i in ans:
        print(i)




if __name__ == '__main__':
    solve()
