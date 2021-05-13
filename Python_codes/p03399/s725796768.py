import sys
IS = lambda: sys.stdin.readline().rstrip()
II = lambda: int(IS())
MII = lambda: list(map(int, IS().split()))
MIIZ = lambda: list(map(lambda x: x-1, MII()))

def main():
    a, b, c, d = [II() for _ in range(4)]
    print(min(a,b)+min(c,d))

if __name__ == '__main__':
    main()
