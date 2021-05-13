import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    w, h, x, y = map(int, input().split())
    if x == 0 or y == 0:
        print(w * h / 2, 0)
    elif w / x == 2 and h / y == 2:
        r = x * h
        print(r, 1)
    else:
        print(w * h / 2, 0)

if __name__ == '__main__':
    main()
