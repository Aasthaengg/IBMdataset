a, b, c = [int(x) for x in input().split(" ")]
i = 0
for y in range(a, b + 1):
    if c % y == 0:
        i += 1
print(i)