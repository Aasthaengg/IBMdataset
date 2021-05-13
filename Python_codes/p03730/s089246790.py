import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    a, b, c = map(int, input().split())

    num = 2
    rem = a % b
    if rem == c:
        print('YES')
        sys.exit()
    while True:
        rem_t = (a * num) % b
        if rem_t == c:
            print('YES')
            sys.exit()
        elif rem_t == rem:
            print('NO')
            sys.exit()
        num += 1

if __name__ == '__main__':
    main()