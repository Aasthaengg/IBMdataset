import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)


def main():
    x, y = map(int, input().split())
    if x == y:
        print(0)
        return
    if x == 0:
        if y < 0:
            print(abs(y) + 1)
            return
        else:
            print(y)
            return
    if x < 0:
        if y > 0:
            if abs(x) < y:
                print(y - abs(x) + 1)
                return
            else:
                print(abs(x) - y + 1)
                return
        elif y == 0:
            print(abs(x))
            return
        else:
            if x > y:
                print(x - y + 2)
                return
            else:
                print(y - x)
                return
    else:
        if y > 0:
            if x < y:
                print(y - x)
                return
            else:
                print(x - y + 2)
                return
        elif y == 0:
            print(x + 1)
            return
        else:
            if x < abs(y):
                print(abs(y) - x + 1)
                return
            else:
                print(x - abs(y) + 1)



if __name__ == "__main__":
    main()
