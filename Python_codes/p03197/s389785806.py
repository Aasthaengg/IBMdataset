import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n = int(input())
    m = map(int, read().split())
    for a in m:
        if a&1:
            print('first')
            sys.exit()
    print('second')


if __name__ == '__main__':
    main()
