def main():
    a, b, c = (int(i) for i in input().split())
    if c <= a + b:
        print(b+c)
    else:
        print(a+b+b+1)


if __name__ == '__main__':
    main()
