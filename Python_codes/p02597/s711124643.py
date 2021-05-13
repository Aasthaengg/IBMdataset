def main():
    n = int(input())
    C = input()

    rc = C.count('R')
    rhc = C[:rc].count('R')
    print(rc - rhc)


if __name__ == '__main__':
    main()
