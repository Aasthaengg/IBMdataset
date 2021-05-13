n, d = map(int, input().split())
c = 0

for i in range(n):
    x, y = map(int, input().split())
    if d*d >= x*x + y*y:
        c = c + 1

print(c)