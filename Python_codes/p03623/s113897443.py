import sys
## io ##
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
def MII(): return list(map(int, IS().split()))
#======================================================#
def main():
    x, a, b = MII()
    print('A' if abs(a-x) < abs(x-b) else 'B')

if __name__ == '__main__':
    main()