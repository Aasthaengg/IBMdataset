a = int(input())
b = int(input())
c = int(input())
d = int(input())

e = [a, b]
f = [c, d]
g = []

for i in e:
    for j in f:
        g.append(i + j)
print(min(g))