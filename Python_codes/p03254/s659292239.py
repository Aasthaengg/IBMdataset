import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(rs())
def rs_(): return [_ for _ in rs().split()]
def ri_(): return [int(_) for _ in rs().split()]

N, x = ri_()
a = sorted(ri_())
ans = 0
for i in range(N):
    if i < N - 1:
        x -= a[i]
        if x >= 0:
            ans += 1
        else:
            break
    else:
        if x == a[i]:
            ans += 1
print(ans)