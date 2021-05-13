import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    x, y = map(int, input().split())
    inf = float('inf')
    r1 = y - x if y - x >= 0 else inf
    r2 = y - -x + 1 if y - -x >= 0 else inf
    r3 = -y - x + 1 if -y - x >= 0 else inf
    r4 = -y - -x + 2 if -y - -x >= 0 else inf
    r = min(r1, r2, r3, r4)
    print(r)

if __name__ == '__main__':
    main()
