def main():
    n = input()

    tmp_sum = 0
    for s in n:
        tmp_sum += int(s)
    print('Yes' if tmp_sum % 9 == 0 else 'No')


if __name__ == '__main__':
    main()
