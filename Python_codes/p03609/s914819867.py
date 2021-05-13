import sys
## io ##
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
def MII(): return list(map(int, IS().split()))

def main():
    x, t = MII()
    print(max(x-t, 0))

if __name__ == '__main__':
    main()