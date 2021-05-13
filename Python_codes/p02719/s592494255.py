def main():
    n, k = map(int, input().split())

    if n == k:
        ans = 0
    elif n > k:
        a = n // k
        ans = min(n - a * k, abs(n - (a + 1) * k))
    elif n < k:
        ans = min(n, k - n)

    print(ans)


if __name__ == "__main__":
    main()
