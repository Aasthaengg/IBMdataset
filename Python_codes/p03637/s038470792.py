if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    count_x2 = 0
    count_x4 = 0

    for aa in a:
        if aa % 4 == 0:
            count_x4 += 1
        elif aa % 2 == 0:
            count_x2 += 1

    if count_x4 >= n//2:
        print('Yes')
        exit()
    tmp = n - count_x2
    if tmp % 2 == 0:
        if count_x4 >= tmp // 2:
            print('Yes')
            exit()
    else:
        if count_x4 >= tmp // 2 + 1:
            print('Yes')
            exit()
    if count_x2 == n:
        print('Yes')
        exit()

    print('No')
