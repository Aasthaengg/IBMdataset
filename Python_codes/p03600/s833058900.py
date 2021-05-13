def main():
    n = int(input())
    d = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            flag = True
            for k in range(n):
                if k == i or k == j:
                    continue
                if d[i][j] > d[i][k]+d[k][j]:
                    print(-1)
                    exit()
                elif d[i][j] == d[i][k]+d[k][j]:
                    flag = False
                else:
                    pass
            if flag:
                ans += d[i][j]
    #print(ans)
    print(ans//2)

if __name__ == '__main__':
    main()
