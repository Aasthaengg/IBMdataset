
def main():
    n, nn, nnn = map(int, input().split(' '))
    print('Yes' if n + nn >= nnn else 'No')

if __name__ == '__main__':
    main()