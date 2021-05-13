def divisor(n):
    res = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res.append((i, n // i))
            if n != i * i:
                res.append((n//i, i))
    return res


if __name__ == "__main__":
    n = int(input())
    d = divisor(n)

    ans = 0
    for x, y in d:
        if y == 1:
            continue
        div, mod = divmod(n, y - 1)
        if div == mod:
            ans += y - 1

    print(ans)
