import sys
rs = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(rs())
rs_ = lambda: [_ for _ in rs().split()]
ri_ = lambda: [int(_) for _ in rs().split()]

N = ri()
a = ri_()
ans = 0
cnt = 0
now = 10000
for i in range(N):
    if a[i] == now:
        cnt += 1
    else:
        ans += -(-cnt//2)
        cnt = 0
        now = a[i]  
ans += -(-cnt//2)
print(ans)