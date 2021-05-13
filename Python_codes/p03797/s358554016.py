def main():
    s, c = list(map(int, input().split()))
    count = 0
    if s <= c//2:
        count = s
    else:
        print(c//2)
        exit()
    c -= s*2
    print(count+c//4)


if __name__ == '__main__':
    main()