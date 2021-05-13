n, x = map(int, input().split())
m = list(int(input()) for _ in range(n))
c = 0
for i in range(n):
    if x < m[i]:
        break
    else:
        x -= m[i]
        c += 1
m.sort()
while x >= m[0]:
    x -= m[0]
    c += 1

print(c)