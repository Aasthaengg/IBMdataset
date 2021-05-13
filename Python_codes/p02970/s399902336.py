import sys
rs = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(rs())
rf = lambda: float(rs())
rs_ = lambda: [_ for _ in rs().split()]
ri_ = lambda: [int(_) for _ in rs().split()]
rf_ = lambda: [float(_) for _ in rs().split()]

N, D = ri_()
print(-(-N//(2*D+1)))