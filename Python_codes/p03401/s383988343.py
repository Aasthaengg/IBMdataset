import sys
IS = lambda: sys.stdin.readline().rstrip()
II = lambda: int(IS())
MII = lambda: list(map(int, IS().split()))
MIIZ = lambda: list(map(lambda x: x-1, MII()))

def main():
    n = II()
    aa = MII()
    aa = [0] + aa + [0]
    g = {i: abs(aa[i+1]-aa[i]) for i in range(n+1)}
    ng = {i: abs(aa[i+2]-aa[i]) for i in range(n)}
    sumv = sum(g.values())
    for i in range(n): print(sumv - (g[i] + g[i+1]) + ng[i])

if __name__ == '__main__':
    main()
