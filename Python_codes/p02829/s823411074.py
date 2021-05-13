import sys
a = []
for l in sys.stdin:
    a.append(int(l))

print(list(set([1,2,3]) - set(a))[0])