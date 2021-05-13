def main():
    n = int(input())
    for i in range(0, n + 1, 7):
        if (n - i) % 4 == 0:
            print('Yes')
            break
    else:
        print('No')


if __name__ == '__main__':
    main()
