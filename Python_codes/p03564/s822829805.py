import sys
IS = lambda: sys.stdin.readline().rstrip()
II = lambda: int(IS())
MII = lambda: list(map(int, IS().split()))
MIIZ = lambda: list(map(lambda x: x-1, MII()))

def main():
    n = II()
    k = II()
    ans = 1
    for i in range(n):
        if ans < k:
            ans *= 2
        else:
            ans += k
    print(ans)

if __name__ == '__main__':
    main()