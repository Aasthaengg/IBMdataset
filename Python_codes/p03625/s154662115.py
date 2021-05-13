n = int(input())
a = list(map(int, input().split()))

l = []
d = dict()
for v in a:
    if v not in d:
        d[v] = 1
    else:
        d[v] += 1
        
    if d[v] == 2 or d[v] == 4:
        l.append(v)

if len(l) < 2:
    print(0)
else:
    l.sort()
    print(l[-1] * l[-2])