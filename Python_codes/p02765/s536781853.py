import sys


def main():
    input = sys.stdin.buffer.readline
    n, r = map(int, input().split()) 
    print(r if n > 9 else r + 100 * (10 - n))



if __name__ == "__main__":
    main()
