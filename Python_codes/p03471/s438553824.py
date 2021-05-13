import sys
 
sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inm = lambda: map(int, sys.stdin.readline().split())
inl = lambda: list(inm())
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))
 
n, y = inm()

discov_flg = False

for a in range(0, n + 1):
    for b in range(0, n + 1 - a):
        c = n - a - b
        total = 10000 * a + 5000 * b + 1000 * c
        if y == total:
            print(f"{a} {b} {c}")
            discov_flg = True
            break
    if discov_flg:
        break
        
if not(discov_flg):
    print("-1 -1 -1")