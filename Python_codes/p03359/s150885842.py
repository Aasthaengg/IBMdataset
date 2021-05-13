def main():
    a, b = map(int, input().split())

    if b < a:
        ans = a - 1
    else:
        ans = a

    print(ans)


if __name__ == "__main__":
    main()
