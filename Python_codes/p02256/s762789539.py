def gdc(x, y):
    if x % y == 0:
        return y
    else:
        return gdc(y, x%y)


if __name__ == '__main__':
    x, y = [int(i) for i in input().split(" ")]
    print(gdc(x, y))