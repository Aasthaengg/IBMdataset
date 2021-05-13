import sys
IS = lambda: sys.stdin.readline().rstrip()
II = lambda: int(IS())
MII = lambda: list(map(int, IS().split()))

def main():
    a,b,c,d = MII()
    if abs(a-c)<=d: print('Yes')
    elif abs(a-b)<=d and abs(b-c)<=d: print('Yes')
    else: print('No')

if __name__ == '__main__':
    main()
