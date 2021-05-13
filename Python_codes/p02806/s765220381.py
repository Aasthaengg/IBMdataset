total = 0
a = int(input())
f = [];
g = [];
for i in range(a):
    b, c = map(str, input().split())
    c = int(c)
    f.append(b)
    g.append(c)
e = input()
h = f.index(e)
j = len(f)
for i in range(j-h-1):
    total += int(g[h+i+1])
print(total)
