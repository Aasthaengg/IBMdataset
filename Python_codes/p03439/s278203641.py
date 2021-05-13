def main():
    N = int(input())

    n_min = 0
    n_max = N-1

    print(n_min)
    tmp_min = input()
    if tmp_min == 'Vacant':
        exit()

    print(n_max)
    tmp_max = input()
    if tmp_max == 'Vacant':
        exit()

    while True:
        n_mid = (n_min + n_max) // 2
        print(n_mid)
        tmp_mid = input()
        if tmp_mid == 'Vacant':
            exit()
        if (n_mid - n_min) % 2 == 0:
            if tmp_min == tmp_mid:
                n_min = n_mid
                tmp_min = tmp_mid
            else:
                n_max = n_mid
                tmp_max = tmp_mid
        else:
            if tmp_min == tmp_mid:
                n_max = n_mid
                tmp_max = tmp_mid
            else:
                n_min = n_mid
                tmp_min = tmp_mid


if __name__ == "__main__":
    main()
