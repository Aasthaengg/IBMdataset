n = int(input())
x, y = map(int, input().split())
p, m = [x+y]*2, [x-y]*2
for i in range(n-1):
    x, y = map(int, input().split())
    p = [min(p[0], x+y), max(p[1], x+y)]
    m = [min(m[0], x-y), max(m[1], x-y)]
print(max(p[1] - p[0], m[1] - m[0]))
