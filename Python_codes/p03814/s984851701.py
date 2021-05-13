import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(rs())
def rs_(): return [_ for _ in rs().split()]
def ri_(): return [int(_) for _ in rs().split()]

s = rs()
f = True
for i in range(len(s)):
    if f and s[i] == 'A':
        a = i
        f = False
    if s[i] == 'Z':
        z = i
print(z - a + 1)