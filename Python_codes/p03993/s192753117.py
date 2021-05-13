import sys
rs = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(rs())
rs_ = lambda: [_ for _ in rs().split()]
ri_ = lambda: [int(_) for _ in rs().split()]

N = ri()
a = [int(_) - 1 for _ in rs().split()]
ans = 0
for i in range(N):
    if a[a[i]] == i:
        ans += 1
print(ans // 2)
