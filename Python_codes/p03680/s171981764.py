import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n, *a = map(int, read().split())
    r = 0
    x = 1
    while x != 2:
        r += 1
        x = a[x - 1]
        if x == 1 or r >= n:
            r = -1
            break
    print(r)

if __name__ == '__main__':
    main()