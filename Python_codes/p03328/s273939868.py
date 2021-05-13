def main():
    a, b = map(int, input().split())
    diff = b - a
    high_a = sum(list(range(1, diff)))
    print(high_a - a)


if __name__ == '__main__':
    main()
