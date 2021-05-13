import sys
input = sys.stdin.readline


def main():
    C = input().strip()
    print(chr(ord(C)+1))


if __name__ == '__main__':
    main()
