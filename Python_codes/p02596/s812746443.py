def calc(k):
    cur = 0
    for i in range(1, 10 ** 7):
        cur *= 10
        cur += 7
        cur %= k
        if cur == 0:
            return i

    return -1


k = int(input())
print(calc(k))