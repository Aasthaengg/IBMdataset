def main():
    a,b = map(int, input().split())

    if b<a:
        print(a-1)
    else:
        print(a)


if __name__ == '__main__':
    main()
