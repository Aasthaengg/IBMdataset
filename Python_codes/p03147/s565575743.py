import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n, *h = map(int, read().split())
    if n == 1:
        print(h[0])
        sys.exit()
    r1 = h[0]
    r2 = h[-1]
    for i1 in range(n - 1):
        if h[i1] < h[i1 + 1]:
            r1 += (h[i1 + 1] - h[i1])
        elif h[i1] > h[i1 + 1]:
            r2 += (h[i1] - h[i1 + 1])
    r = max(r1, r2)
    print(r)
if __name__ == '__main__':
    main()
