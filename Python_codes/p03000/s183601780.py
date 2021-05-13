n, x = list(map(int, input().split()))
l = list(map(int, input().split()))

c = 1
y = 0

for m in l:
    if y + m <= x:
        c += 1
        y += m
    else:
        break

print(c)

