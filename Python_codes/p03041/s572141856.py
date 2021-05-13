def main():
    n,k = map(int, input().split())
    k-=1
    s = list(input().rstrip())

    s[k]=s[k].lower()
    print(''.join(s))


if __name__ == '__main__':
    main()
