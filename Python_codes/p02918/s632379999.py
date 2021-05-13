def main():
    n, k = map(int, input().split())
    s = list("*" + input() + "*")
    count = 0
    for i in range(1, n + 1):
        if (s[i] == s[i - 1] == "L") or (s[i] == s[i + 1] == "R"):
            count += 1
    print(min(count + 2 * k, n - 1))


if __name__ == '__main__':
    main()

