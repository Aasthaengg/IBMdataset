def main():
    x,y = map(int, input().split())

    if y>=x:
        print(min(y-x,abs(y+x)+1))
    else:
        print(min(abs(y+x)+1,abs(y-x)+2))


if __name__ == '__main__':
    main()