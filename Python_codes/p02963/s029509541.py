if __name__ == '__main__':
    s = int(input())
    m = 10 ** 9
    x = (m - s % m) % m
    y = (s + x) // m
    print("0 0 1000000000 1 {} {}".format(x, y))
