import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    x, y = map(int, input().split())
    for i1 in range(x + 1):
        if i1 * 2 + (x - i1) * 4 == y:
            print('Yes')
            sys.exit()
    print('No')

if __name__ == '__main__':
    main()
