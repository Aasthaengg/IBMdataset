if __name__ == '__main__':
    n, k = map(int, input().split())
    if k % 2 == 1:
        base = n // k
        if base == 0:
            print(0)
        else:
            print(base ** 3)
    else:
        ans = 0
        base = n // k
        if base != 0:
            ans += base ** 3

        base = n // (k // 2)
        if base % 2 == 0:
            base = base // 2
        else:
            base = (base + 1) // 2

        ans += base ** 3

        print(ans)