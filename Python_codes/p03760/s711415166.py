import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(rs())
def rs_(): return [_ for _ in rs().split()]
def ri_(): return [int(_) for _ in rs().split()]

o = rs()
e = rs()
ans = ''
for i in range(len(o)):
    ans += o[i]
    if i < len(e):
        ans += e[i]
print(ans)