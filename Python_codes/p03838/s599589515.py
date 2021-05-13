def main():
    x, y = map(int, input().split())

    if x == y:
        print(0)

    elif abs(x) == abs(y):
        print(1)

    elif x < y:
        if x >= 0 and y >= 0:
            print(y - x)

        elif x >= 0 and y <= 0:
            pass

        elif x <= 0 and y >= 0:
            if y == 0:
                print(abs(x))
            else:
                if abs(y) > abs(x):
                    print(abs(y) - abs(x) + 1)
                else:
                    print(abs(x) - abs(y) + 1)

        elif x <= 0 and y <= 0:
            print(abs(x) - abs(y))

    elif x > y:
        if x <= 0 and y <= 0:
            c1 = abs(y) - x + 1
            c2 = abs(y) - abs(x) + 2
            print(min(c1, c2))

        elif x <= 0 and y >= 0:
            pass

        elif x >= 0 and y <= 0:
            print(max(abs(x), abs(y)) - min(abs(x), abs(y)) + 1)
            
        elif x >= 0 and y >= 0:
            print(x - y + 2)

if __name__ == "__main__":
    main()