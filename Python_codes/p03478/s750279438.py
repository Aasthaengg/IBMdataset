import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n, a, b = map(int, input().split())
    r = 0
    for i1 in range(1, n + 1):
        i1sum = 0
        i1org = i1
        while i1:
            i1sum += i1 % 10
            i1 = i1 // 10
        if a <= i1sum <= b:
            r += i1org
    print(r)

if __name__ == '__main__':
    main()
