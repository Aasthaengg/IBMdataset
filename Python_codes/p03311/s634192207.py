import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n, *a = map(int, read().split())

    a2 = list([ea - i - 1 for i, ea in enumerate(a)])
    a2.sort()
    n2 = n // 2
    r1 = sum([abs(ea2 - a2[n2]) for ea2 in a2])
    r2 = sum([abs(ea2 - a2[n2-1]) for ea2 in a2])
    print(min(r1, r2))


if __name__ == '__main__':
    main()