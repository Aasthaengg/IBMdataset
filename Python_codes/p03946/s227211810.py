from collections import Counter
n,t = map(int, input().split())
a = list(map(int, input().split()))

mx = 0
b = []
for i in a[::-1]:
    if mx < i:
        mx = i
    b.append(mx-i if i < mx else 0)
c = Counter(b)

print(c[max(c.keys())])
