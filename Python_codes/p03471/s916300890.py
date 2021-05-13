def main():
    n, y = map(int, input().split())
    flag = False

    a = -1
    b = -1
    c = -1

    for i in range(0, n + 1):
        for j in range(0, n + 1):

            money = y - 10000 * i - 5000 * j
            k = n - (i + j)
            if k < 0:
                break
            else:
                if 1000 * k == money:
                    a = i
                    b = j
                    c = k
                    flag = True
                    break

        if flag:
            break

    print(a, b, c)


if __name__ == '__main__':
    main()