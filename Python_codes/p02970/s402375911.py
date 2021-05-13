n, d = map(int, input().split())

quotient = n // (2 * d + 1)
surplus = n % (2 * d + 1)

if surplus == 0:
    print(quotient)
else:
    print(quotient + 1)
