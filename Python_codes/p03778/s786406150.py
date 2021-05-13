def main():
    W, a, b = map(int, input().split())
    if a <= b:
        if a + W >= b:
            print(0)
        else:
            print(b - a - W)
    else:
        if b + W >= a:
            print(0)
        else:
            print(a - b - W)


if __name__ == '__main__':
    main()
