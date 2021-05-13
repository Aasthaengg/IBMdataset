import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    a, b, x = map(int, input().split())
    r = (b // x) + 1
    if b > 0:
        r -= ((a - 1) // x) + 1
    print(r)

if __name__ == '__main__':
    main()