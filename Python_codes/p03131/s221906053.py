def main():
    k, a, b = map(int, input().split())
    cookie = 1
    if b <= a + 1 or 1 + k <= a:
        cookie += k
    else:
        cookie += a - 1
        k -= a - 1
        if k % 2:
            k -= 1
            cookie += 1
        cookie += (b - a) * max(0, k // 2)
    print(cookie)


if __name__ == '__main__':
    main()

