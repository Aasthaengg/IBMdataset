a, b = map(int, input().split())

c = b - a
s = 0
for i in range(c + 1):
    s += i

print(s - b)
