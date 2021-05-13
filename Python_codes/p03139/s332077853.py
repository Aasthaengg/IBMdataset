def main():
    n, a, b = map(int, input().split())

    max_num = min(a, b)
    min_num = max(0, a + b - n)

    print(max_num, min_num)


if __name__ == "__main__":
    main()
