n = int(input())
t, a = map(int, input().split())
for i in range(1, n):
    x, y = map(int, input().split())
    i = max(t // x, a // y)
    c, d = x, y
    while c < t or d< a:
        c = x * i
        d = y * i
        i += 1
    t, a = c, d
print(t + a)