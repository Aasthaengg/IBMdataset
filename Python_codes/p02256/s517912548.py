def greatest_common_divisor(x, y):
    if x < y:
        x, y = y, x

    if y == 0:
        return x
    else:
        return greatest_common_divisor(y, x % y)

if __name__ == '__main__':
    x, y = [int(x) for x in input().split()]
    print(greatest_common_divisor(x, y))