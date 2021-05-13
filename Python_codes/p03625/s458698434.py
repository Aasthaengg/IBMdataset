from collections import Counter, deque
n = int(input())
a = list(map(int, input().split()))
b = Counter(a)
c = deque([])
for k in b.keys():
    if b[k]>=4:
        c.append(k)
        c.append(k)
    elif b[k]>=2:
        c.append(k)
c = sorted(c, reverse = True)
print(c[0]*c[1] if c else 0)