import sys
## io ##
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
def MII(): return list(map(int, IS().split()))
#======================================================#
def main():
    n, k = MII()
    aa = MII()
    print((-(-(n-1)//(k-1))) if n > 3 else 1)


if __name__ == '__main__':
    main()