def main():
    s = list(input())
    n = len(s)
    ans = ''
    for i in range(n):
        if i % 2 == 0:
            ans += s[i]
    print(ans)


if __name__ == "__main__":
    main()
