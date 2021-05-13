def main():
    s = input()
    n = len(s)
    ans = 100000000
    for i in range(2, n):
        t = int(s[i - 2: i+1])
        ans = min(ans, abs(753 - t))
    print(ans)


if __name__ == '__main__':
    main()
