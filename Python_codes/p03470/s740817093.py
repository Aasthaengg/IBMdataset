import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n = int(input())
    d = set(map(int, readlines()))
    print(len(d))


if __name__ == '__main__':
    main()
