def main():
    a, b, c, k = map(int, input().split())

    if k <= a:
        ans = k
    elif a < k and k <= a + b:
        ans = a
    else:
        ans = a - (k - (a + b))

    print(ans)


if __name__ == "__main__":
    main()
