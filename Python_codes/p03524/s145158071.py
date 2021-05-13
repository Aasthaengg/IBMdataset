import collections

s = input()
d = collections.Counter(s)
if len(d) < 3:
    num = max(d.values())
else:
    num = max(d.values()) - min(d.values())
print('YES' if num<2 else 'NO')