import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    x, y = map(int, input().split())
    if x < y:
        if y == 0:
            print(-x)
        elif x == 0:
            print(y)
        elif 0 < x and 0 < y:
            print(y - x)
        elif x < 0 and 0 < y:
            print(abs(y - abs(x)) + 1)
        else:
            print(y - x)
    else:
        if y == 0:
            print(x + 1)
        elif x == 0:
            print(-y + 1)
        elif 0 < y and 0 < x:
            print(x - y + 2)
        elif y < 0 and 0 < x:
            print(abs(x - abs(y)) + 1)
        else:
            print((x - y) + 2)

if __name__ == '__main__':
    main()
