def judge1(lst):
    flag = False
    if lst[-1] == lst[-2]:
        flag = True
    return flag


def main():
    lst = list(map(int, input().split()))
    lst.sort()
    count = 0

    while True:
        if judge1(lst):
            break

        lst[0] += 1
        lst[1] += 1
        count += 1

    while lst[2] - lst[0] >= 2:
        lst[0] += 2
        count += 1

    if lst[2] - lst[0] == 1:
        count += 2

    print(count)


if __name__ == '__main__':
    main()