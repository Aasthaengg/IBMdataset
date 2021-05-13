import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(rs())
def rs_(): return [_ for _ in rs().split()]
def ri_(): return [int(_) for _ in rs().split()]

N = ri()
S = rs()
x = 0
ans = 0
for s in S:
    if s == 'I':
        x += 1
    else:
        x -= 1
    ans = max(ans, x)
print(ans)