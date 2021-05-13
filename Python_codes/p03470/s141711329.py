n = int(input())
d = []
for _ in range(n):
    d.append(int(input()))
d.sort()
a = 1
for i in range(len(d) - 1):
    if d[i] < d[i + 1]:
        a += 1
print(a)