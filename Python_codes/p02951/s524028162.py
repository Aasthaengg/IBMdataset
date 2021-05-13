def main():
    a, b, c = (int(i) for i in input().split())
    d = a-b
    print(max(0, c - d))


if __name__ == '__main__':
    main()
