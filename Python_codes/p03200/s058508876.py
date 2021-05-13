def main():
    s = input()
    count = 0
    black_count = 0
    for i in range(len(s)):
        if s[i] == 'B':
            black_count += 1
        if s[i] == 'W':
            count += black_count

    print(count)


if __name__ == "__main__":
    main()
