import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(rs())
def rs_(): return [_ for _ in rs().split()]
def ri_(): return [int(_) for _ in rs().split()]

A = ri()
B = ri()
print('GREATER' if A > B else 'LESS' if A < B else 'EQUAL')