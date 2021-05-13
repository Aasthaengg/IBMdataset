import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n, k = map(int, input().split())
    if n == 1:
        print(k)
        sys.exit()
    r = k
    r *= pow(k - 1, n - 1)
    print(r)

if __name__ == '__main__':
    main()