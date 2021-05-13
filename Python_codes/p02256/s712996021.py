def main() :
    x, y = [int(d) for d in input().split()]
    while y != 0 :
        x, y = y, x%y

    print(x)

if __name__ == '__main__' :
    main()