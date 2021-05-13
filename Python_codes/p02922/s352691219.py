a, b = list(map(int, input().split()))
c = 0
out = 1
while out < b:
    out -= 1
    out += a
    c += 1
print(c)