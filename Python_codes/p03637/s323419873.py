def main():
    n = int(input())
    a = [int(an) for an in input().split()]
    exist2 = False
    not4 = 0
    count4 = 0
    for an in a:
        if an % 2 == 0:
            if an % 4 == 0:
                count4 += 1
            else:
                if not exist2:
                    exist2 = True
                    not4 += 1
        else:
            not4 += 1
    print('Yes' if count4 >= not4 - 1 else 'No')


if __name__ == '__main__':
    main()
