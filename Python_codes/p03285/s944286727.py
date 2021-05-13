import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n = int(input())
    num = 0
    while num <= n:
        if (n - num) % 7 == 0:
            print('Yes')
            sys.exit()
        num += 4
    print('No')


if __name__ == '__main__':
    main()