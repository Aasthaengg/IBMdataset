def main():
    n = int(input())
    if n % 2:
        print(0)
    else:
        n //= 2
        ans = 0
        i = 5
        while i <= n:
            ans += n // i
            i *= 5
        print(ans)


if __name__ == '__main__':
    main()

