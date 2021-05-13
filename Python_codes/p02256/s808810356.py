def greatest_common_divisor(x, y):
    while True:
        if x == 0 or y == 0:
            break
        elif x >= y:
            x %= y
        else:
            y %= x

    return x+y

if __name__ == '__main__':
    x, y = map(int, input().split())
    gcd = greatest_common_divisor(x, y)
    print(gcd)

