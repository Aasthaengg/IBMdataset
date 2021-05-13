import sys
rs = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(rs())
rf = lambda: float(rs())
rs_ = lambda: [_ for _ in rs().split()]
ri_ = lambda: [int(_) for _ in rs().split()]
rf_ = lambda: [float(_) for _ in rs().split()]

A, B = ri_()
ans = 'IMPOSSIBLE'
if (A + B) % 2 == 0:
    ans = (A + B) // 2
print(ans)