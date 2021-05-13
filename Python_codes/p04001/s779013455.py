import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(rs())
def rs_(): return [_ for _ in rs().split()]
def ri_(): return [int(_) for _ in rs().split()]
s = rs()
n = len(s)
ans = 0
for bit in range(1 << n - 1):
    tmp = 0
    for i in range(n - 1):
        if bit & (1 << i):
            ans += int(s[tmp:i+1])
            tmp = i + 1
    ans += int(s[tmp:n])
print(ans)