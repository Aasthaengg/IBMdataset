def main():
    n, k = map(int, input().split())

    if n % 2 == 1:
        n += 1

    if n // 2 >= k:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
