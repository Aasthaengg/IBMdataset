def main():
    s = list(input())
    ans = 0
    a = 0
    for i in range(len(s)):
        if s[i] == 'W':
            ans += i - a
            a += 1
    print(ans)

if __name__ == '__main__':
    main()
