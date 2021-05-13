def main():
    n, a, b = [int(i) for i in input().split()]
    print('Alice' if (max(a,b)-min(a,b)-1)%2 == 1 else 'Borys')


if __name__ == '__main__':
    main()