def main():
    n, a, b = map(int, input().split())

    c = n // (a + b)
    d = n % (a + b)

    if d > a:
        ans = a * c + a
    else:
        ans = a * c + d

    print(ans)


if __name__ == "__main__":
    main()
