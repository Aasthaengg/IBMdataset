def gcd(x, y):
    if x > y:
        return gcd(y, x)
    if y % x == 0:
        return x
    else:
        return gcd(y % x, x)


def main():
    x, y = map(int, input().split())
    print(gcd(x,y))

if __name__ == "__main__":
    main()