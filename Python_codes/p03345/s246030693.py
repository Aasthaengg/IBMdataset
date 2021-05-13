def main():
    a, b, c, k = map(int, input().split())

    ans = (-1) ** (k % 2) * (a - b)

    print(ans)


if __name__ == "__main__":
    main()
