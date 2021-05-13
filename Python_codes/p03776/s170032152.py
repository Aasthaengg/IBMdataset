import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def nCr(n, r):
    return fac[n] // fac[r] // fac[n - r]

fac = [1]
for i in range(1, 51):
    fac.append(fac[-1] * i)

def main():
    n, a, b = MI()
    vv = LI()
    vv.sort(reverse=True)
    s = sum(vv[:a])
    tot = vv.count(vv[a - 1])
    l = vv[:a].count(vv[a - 1])
    if l == a:
        p = 0
        for r in range(l, min(tot,b) + 1):
            p += nCr(tot, r)
    else:
        p = nCr(tot, l)
    print(s / a)
    print(p)

main()
