import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    A = int(input())

    print(N**2 - A)


if __name__ == '__main__':
    main()
