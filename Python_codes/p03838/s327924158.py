def main():
    x, y = list(map(int, input().split()))
    ans = abs(y) - abs(x)
    if x > 0 and y > 0 or x < 0 and y < 0:
        if x > y:
            print(x - y + 2)
        else:
            print(y - x)
    elif x < 0 and y >= 0:
        print(min(y - x, abs(y - abs(x)) + 1))
    elif x >= 0 and y < 0:
        print(abs(x - abs(y)) + 1)
    elif x == 0 and y > 0:
        print(y - x)
    else:
        print(x + 1)


if __name__ == '__main__':
    main()
