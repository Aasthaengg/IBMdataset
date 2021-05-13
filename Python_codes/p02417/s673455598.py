import sys
cs = { c : 0 for c in list("abcdefghijklmnopqrstuvwxyz")}
for c in list(sys.stdin.read()):
    c = c.lower()
    if c in cs.keys():
        cs[c] = cs[c] + 1
for (c,cnt) in sorted(list(cs.items())):
    print('{0} : {1}'.format(c,cnt))