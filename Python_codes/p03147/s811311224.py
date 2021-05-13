import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n, *h = map(int, read().split())
    if n == 1:
        print(h[0])
        sys.exit()
    r1 = h[0]
    for i1 in range(n - 1):
        if h[i1] < h[i1 + 1]:
            r1 += (h[i1 + 1] - h[i1])
    print(r1)
if __name__ == '__main__':
    main()