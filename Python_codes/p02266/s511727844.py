import sys

s1 = []
s2 = []
area = []

for i, c in enumerate(sys.stdin.readline()[:-1]):
    if c == '\\':
        s1.append(i)
    elif c == '/' and len(s1) > 0:
        j = s1.pop()
        a = i - j
        while s2:
            if s2[-1] > j:
                s2.pop()
                a += area.pop()
            else:
                break
        s2.append(j)
        area.append(a)

print(sum(area))
print(len(area), *area)