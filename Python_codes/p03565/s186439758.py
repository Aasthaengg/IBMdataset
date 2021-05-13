import re
s, t = input().replace(*"?."), input()
l, m = len(s), len(t)

can = []
for i in range(l - m + 1):
    if re.match(s[i:i+m], t):
        can += (s[:i] + t + s[i+m:]).replace(*".a"),
print(min(can) if can else "UNRESTORABLE")