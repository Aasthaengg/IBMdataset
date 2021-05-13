import sys
IS = lambda: sys.stdin.readline().rstrip()
II = lambda: int(IS())
MII = lambda: list(map(int, IS().split()))

def main():
    abc = MII()
    k = II()
    maxv = max(abc)
    sumv = sum(abc) - maxv
    for i in range(k):
        maxv *= 2
    sumv += maxv
    print(sumv)


if __name__ == '__main__':
    main()
