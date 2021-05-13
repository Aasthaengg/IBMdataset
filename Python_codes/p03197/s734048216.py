import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a2 = [ae&1 ^ 1 for ae in a]
    if all(a2):
        print('second')
    else:
        print('first')


if __name__ == '__main__':
    main()
