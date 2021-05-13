def kiriage(price):
    i = int(price) / 1000
    r = price % 1000
    if r != 0:
        return 1000 * (i + 1)
    else:
        return 1000 * i

if __name__ == '__main__':
    n = int(raw_input())
    price = 100000
    for i in range(0, n):
        price = kiriage(price * 1.05)
    print price