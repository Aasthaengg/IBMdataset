import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(rs())
def rs_(): return [_ for _ in rs().split()]
def ri_(): return [int(_) for _ in rs().split()]

a = ri_()
print(min((a[0] % 2) * (a[1] * a[2]), (a[1] % 2) * (a[0] * a[2]), (a[2] % 2) * (a[0] * a[1])))