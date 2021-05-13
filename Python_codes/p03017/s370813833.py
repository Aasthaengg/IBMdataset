def main():
    n, a, b, c, d = map(int, input().split())
    s = input()
    s = '.' + s

    if '##' in s[a+1:c] or '##' in s[b+1:d]:
        print('No')
    else:
        if c < b:
            print('Yes')
        elif c < d:
            print('Yes')
        else:
            if '...' in s[b-1:d+2]:
                print('Yes')
            else:
                print('No')


if __name__ == '__main__':
    main()
