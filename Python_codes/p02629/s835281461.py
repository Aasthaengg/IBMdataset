def abc171c_one_quadrillion():
    n = int(input())
    s = ''
    while n > 26:
        i = 0
        total = 1
        while total <= n:
            i += 1
            total += pow(26, i)
        total -= pow(26, i)
        i -= 1

        val = min(25, (n - total) // pow(26, i))
        s += chr(64 + val + 1)
        n -= (val + 1) * pow(26, i)

    s += chr(64 + n)
    s = s.lower()
    print(s)

abc171c_one_quadrillion()