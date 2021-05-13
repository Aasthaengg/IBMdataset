x, y = map(int, input().split())
c = 0
curr = x
for q in range(x, y + 1):
    curr *= 2
    c += 1
    if curr > y:
        break
print(c)