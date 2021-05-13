a, b = map(int, input().split())
count = 0
for i in range(a, b + 1):
    c = str(i)
    if c[0] == c[4] and c[1] == c[3]:
        count += 1
print(count)