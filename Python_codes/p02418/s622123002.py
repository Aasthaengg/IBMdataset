import sys
s = input()
ls = len(s)
s += s
p = input()
lp = len(p)
for i in range(ls):
    if s[i:i + lp] == p:
        print('Yes')
        sys.exit()
print('No')
