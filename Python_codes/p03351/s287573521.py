def main():
    a,b,c,d = map(int, input().split())

    if abs(a-c)<=d or (abs(a-b)<=d and abs(b-c)<=d):
        print('Yes')
        return
    print('No')


if __name__ == '__main__':
    main()