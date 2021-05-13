import sys


# input = sys.stdin.readline

def main():
    N = int(input())
    eve = int(N//2)
    print((N-eve)/N)


if __name__ == "__main__":
    main()