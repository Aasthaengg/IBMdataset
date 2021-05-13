import sys
IS = lambda: sys.stdin.readline().rstrip()
II = lambda: int(IS())
MII = lambda: list(map(int, IS().split()))

def main():
    a, b, x = MII()
    if x < a: print('NO')
    elif x <= a+b: print('YES')
    else: print('NO')

if __name__ == '__main__':
    main()
