import sys
IS = lambda: sys.stdin.readline().rstrip()
II = lambda: int(IS())
MII = lambda: list(map(int, IS().split()))

def main():
    a, b = MII()
    cnt = a-1
    if b>=a: cnt+=1
    print(cnt)

if __name__ == '__main__':
    main()
