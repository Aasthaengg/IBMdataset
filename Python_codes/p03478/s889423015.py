import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n, a, b = map(int, input().split())
    r = 0
    for i1 in range(1, n + 1):
        i1sum = sum(tuple(map(int, str(i1))))
        if a <= i1sum <= b:
            r += i1
    print(r)

if __name__ == '__main__':
    main()