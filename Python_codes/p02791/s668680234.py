n = int(input())
p = list(map(int, input().split()))
m = [p[0]]
c = 1
for i in range(1, n):
    m.append(min(m[i - 1], p[i]))
    if m[i] == p[i]:
        c += 1
print(c)