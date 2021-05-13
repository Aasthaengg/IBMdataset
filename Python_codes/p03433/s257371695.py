import sys
IS = lambda: sys.stdin.readline().rstrip()
II = lambda: int(IS())
MII = lambda: list(map(int, IS().split()))
MIIZ = lambda: list(map(lambda x: x-1, MII()))

def main():
    n = II()
    a = II()
    if n%500 <= a: print('Yes')
    else: print('No')

if __name__ == '__main__':
    main()
