import sys
IS = lambda: sys.stdin.readline().rstrip()
II = lambda: int(IS())
MII = lambda: list(map(int, IS().split()))
MIIZ = lambda: list(map(lambda x: x-1, MII()))

def main():
    r = II()
    g = II()
    print(2*g-r)

if __name__ == '__main__':
    main()