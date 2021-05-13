n = int(input())
p = list(map(int, input().split()))
x = p[0]
y = 0
for i in range(n):
    x = min(x, p[i])
    if x == p[i]:
        y += 1

print(y)