import sys
IS = lambda: sys.stdin.readline().rstrip()
II = lambda: int(IS())
MII = lambda: list(map(int, IS().split()))

def main():
    a, b = MII()
    if b%a == 0: print(a+b)
    else: print(b-a)

if __name__ == '__main__':
    main()
