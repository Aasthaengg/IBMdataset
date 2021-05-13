N = int(input())
d = []
d.append(int(input()))
a = 1
for _ in range(N-1):
    i = int(input())
    w = True
    for j in range(a):
        if i == d[j]:
            w = False
    if w:
        d.append(i)
        a += 1
print(a)
