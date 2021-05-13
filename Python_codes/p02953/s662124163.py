import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n, *h = map(int, read().split())
    for i1 in range(n - 1, 0, -1):
        if h[i1] >= h[i1-1]:
            pass
        elif h[i1] == h[i1-1] - 1:
            h[i1-1] -= 1
        else:
            print('No')
            sys.exit()
    print('Yes')

if __name__ == '__main__':
    main()