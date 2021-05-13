def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    non_negative = len(list(filter(lambda x: x >= 0, a)))
    negative = n - non_negative
    if non_negative == 0:
        negative = n - 1
        non_negative = 1
    elif negative == 0:
        negative = 1
        non_negative = n - 1
    neg_num = a[:negative]
    non_neg_num = a[-non_negative:]
    ope = []
    for nnn in non_neg_num[:-1]:
        ope.append([neg_num[0], nnn])
        neg_num[0] -= nnn
    for nn in neg_num:
        ope.append([non_neg_num[-1], nn])
        non_neg_num[-1] -= nn
    print(non_neg_num[-1])
    for i, j in ope:
        print(i, j)


if __name__ == '__main__':
    main()
