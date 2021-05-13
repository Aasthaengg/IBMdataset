def main():
    n = int(input())
    A = list(map(int, input().split()))
    n2 = sum([a % 2 == 0 for a in A])
    n4 = sum([a % 4 == 0 for a in A])
    nodd = n - n2
    n2 -= n4
    if nodd == n4 + 1:
        if n2 == 0:
            print('Yes')
        else:
            print('No')
    elif nodd <= n4:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
