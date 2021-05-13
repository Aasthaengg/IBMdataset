n = int(input())
p = []
for i in range(n):
    pp = int(input())
    p.append(pp)
p.sort()
print(sum(p) - p[n - 1] // 2)
