n = int(input())
p = []
for _ in range(n):
    p.append(int(input()))
p.sort()
a = 0
for i in range(n):
    if i == n - 1:
        a += p[i] // 2
    else:
        a += p[i]
print(a)