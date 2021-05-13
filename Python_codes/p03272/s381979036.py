import sys
IS = lambda: sys.stdin.readline().rstrip()
II = lambda: int(IS())
MII = lambda: list(map(int, IS().split()))

def main():
    n, i = MII()
    print(n-i+1)

if __name__ == '__main__':
    main()
