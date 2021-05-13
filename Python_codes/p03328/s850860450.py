def main():
    a, b = map(int, input().split())
    print(sum(list(range(1, b - a))) - a)


if __name__ == '__main__':
    main()
