r = 0
for i in range(1, int(input()) + 1):
    if i % 3 > 0 and i % 5 > 0:
        r += i

print(r)
