def main():
    s = input()
    n = len(s)
    min_diff = 1000

    for i in range(n - 2):
        diff = abs(int(s[i: i+3]) - 753)
        if diff < min_diff:
            min_diff = diff

    print(min_diff)


if __name__ == "__main__":
    main()
