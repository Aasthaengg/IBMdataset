import sys
read = sys.stdin.read
def main():
    a, b, m = map(int, input().split())
    al = tuple(map(int, input().split()))
    bl = tuple(map(int, input().split()))
    r = min(al) + min(bl)
    m = map(int, read().split())
    xyc = zip(m, m, m)
    for x, y, c in xyc:
        r = min(r, al[x-1] + bl[y-1] - c)
    print(r)

if __name__ == '__main__':
    main()