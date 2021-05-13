def main():
    # n = int(input())
    n, m = map(int, input().split())
    # v = list(map(int, input().split()))
    # s = input()
    py = []
    for i in range(m):
        p, y = map(int, input().split())
        py.append([i, p, y])

    py.sort(key=lambda x: (x[1], x[2]))

    num = 1
    for i in range(0, m):
        if i == 0:
            py[i].append(num)
        else:
            if py[i][1] == py[i-1][1]:
                num += 1
            else:
                num = 1
            py[i].append(num)

    py.sort(key=lambda x: x[0])

    for i in range(m):
        print(str(py[i][1]).zfill(6) + str(py[i][3]).zfill(6))


if __name__ == '__main__':
    main()
