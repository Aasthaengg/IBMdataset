def main():
    n = int(input())

    if n == 1 or n == 2:
        ans = 0
    else:
        if n % 2 == 0:
            ans = n // 2 - 1
        else:
            ans = n // 2

    print(ans)


if __name__ == "__main__":
    main()
