def main():
    n, t, *a = map(int, open(0).read().split())
    b = 0
    c = float("Inf")
    ans = 1
    for i in range(n):
        x = a[i]
        ans = 1 if x - c > b else ans + int(x - c == b)
        b = max(b, x - c)
        c = min(c, x)

    print(ans)


if __name__ == '__main__':
    main()
