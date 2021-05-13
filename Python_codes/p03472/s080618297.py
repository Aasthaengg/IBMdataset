n, h = map(int, input().split())
ab = []
for i in range(n):
    a, b = map(int, input().split())
    ab.append((a, "a"))
    ab.append((b, "b"))

ab.sort(reverse=True, key=lambda x: x[0])
#print(ab)
count = 0
for x, y in ab:
    if h <= 0:
        break
    if y == "a":
        if h%x == 0:
            count += h//x
            h = 0
        else:
            count += h//x + 1
            h = 0
    if y == "b":
        h -= x
        count += 1

print(count)