def main():
    x, n = map(int, input().split())
    p_lst = list(map(int, input().split()))

    if n == 0:
        minimum = x
    else:
        if x not in p_lst:
            minimum = x

        else:
            lst = []
            flag = False
            x1 = x
            x2 = x

            while True:
                x1 += 1
                x2 -= 1

                if x1 not in p_lst:
                    lst.append(x1)
                    flag = True
                if x2 not in p_lst:
                    lst.append(x2)
                    flag = True

                if flag:
                    break

            minimum = min(lst)

    print(minimum)


if __name__ == '__main__':
    main()