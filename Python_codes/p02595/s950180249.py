import sys
read = sys.stdin.read
#readlines = sys.stdin.readlines
def main():
    n, d = map(int, input().split())
    r = 0
    m = map(int, read().split())
    ab = zip(m, m)
    d2 = d**2
    for a, b in ab:
        r += (a ** 2 + b ** 2) <= d2
    print(r)

if __name__ == '__main__':
    main()