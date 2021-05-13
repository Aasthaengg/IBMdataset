a, b, t = map(int, input().split())
m = 0
i = 1

while i * a < t + 0.5:
    i += 1
    m += b

print(m)