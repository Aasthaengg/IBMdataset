import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(rs())
def rs_(): return [_ for _ in rs().split()]
def ri_(): return [int(_) for _ in rs().split()]

N = ri()
T = ri_()
M = ri()
wa = sum(T)
for _ in range(M):
    P, X = ri_()
    ans = wa + X - T[P - 1]
    print(ans)