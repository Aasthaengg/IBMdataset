s = int(input())
d = set()
i = 1
while s not in d:
    d.add(s)
    s = 3 * s + 1 if s & 1 else s // 2
    i += 1
print(i)
