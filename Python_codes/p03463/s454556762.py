import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n, a, b = map(int, input().split())
    if abs(a - b)&1:
        print('Borys')
    else:
        print('Alice')

if __name__ == '__main__':
    main()