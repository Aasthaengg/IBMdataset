import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n, *a = map(int, read().split())
    r = len(set(a))
    r -= (n - r)&1
    print(r)

if __name__ == '__main__':
    main()