def gcd(x, y):
    if x < y:
        tmp = x
        x = y
        y = tmp

    while y > 0:
        r = x % y
        x = y
        y = r

    return x

if __name__ == "__main__":
    x, y = map(int, input().split())
    print(gcd(x, y))