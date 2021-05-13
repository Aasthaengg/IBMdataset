def main():
    n = int(input())
    a = [[int(x) for x in input().split()] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if a[i][j] > a[i][k] + a[k][j]:
                    print(-1)
                    return

    ret = 0
    for i in range(n):
        for j in range(i):
            for k in range(n):
                if k == i or k == j: continue
                if a[i][j] == a[i][k] + a[k][j]: break  # 辺ではない
            else:
                ret += a[i][j]

    print(ret)


if __name__ == '__main__':
    main()
