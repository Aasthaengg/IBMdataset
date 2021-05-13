import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

def main():
    L,R,d = map(int, readline().split())

    print(R // d - (L - 1) // d)


if __name__ == "__main__":
    main()
