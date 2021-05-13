import sys
read = sys.stdin.read
readlines = sys.stdin.readlines

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s = set(s)
    r = len(s)
    print(r)


if __name__ == '__main__':
    main()
