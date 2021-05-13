import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n, *a = map(int, read().split())
    if sum(a)&1:
        print('NO')
    else:
        print('YES')

if __name__ == '__main__':
    main()
