def main():
    a, b, c, K = (int(i) for i in input().split())
    if K & 1:
        print(b-a)
    else:
        print(a-b)


if __name__ == '__main__':
    main()
