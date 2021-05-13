from collections import Counter
n = int(input())
a = list(map(int, input().split()))

c = Counter(a)

e = []
for k, v in c.items():
    if v > 3:
        e.append(k)
        e.append(k)
    elif v > 1:
        e.append(k)
e.sort(reverse=True)

if len(e)<2:
    print(0)
else:
    print(e[0]*e[1])