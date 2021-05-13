def main():
    a, b, c = map(int, input().split())
    c -= min(c, a - b)
    print(c)


if __name__ == '__main__':
    main()

