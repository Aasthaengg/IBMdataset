def main():
    n = int(input())
    a_lst = [int(input()) for _ in range(n)]
    a_lst.sort()

    count = 0
    tmp = 0
    number = a_lst[0]

    for i in range(n):

        if a_lst[i] == number:
            tmp += 1

            if i == n - 1:
                if tmp % 2 != 0:
                    count += 1

        else:
            number = a_lst[i]

            if tmp % 2 == 0:
                tmp = 1
                continue
            else:
                count += 1
                tmp = 1

    if n > 1:
        if a_lst[-1] != a_lst[-2]:
            count += 1

    print(count)


if __name__ == '__main__':
    main()