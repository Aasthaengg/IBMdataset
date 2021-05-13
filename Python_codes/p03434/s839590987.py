import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n, *a = map(int, read().split())
    a.sort(reverse=True)
    alice = sum(a[::2])
    bob = sum(a[1::2])
    print(alice - bob)


if __name__ == '__main__':
    main()
