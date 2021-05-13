def main():
    a, b, c = (int(i) for i in input().split())
    from math import sqrt
    s = (a + b + c) / 2
    print(int(sqrt(s*(s-a)*(s-b)*(s-c))))


if __name__ == '__main__':
    main()
