a, b = map(int, input().split(" "))
count = 0
for v in range(a, b + 1):
    v1 = v % 10
    v2 = v // 10 % 10
    v3 = v // 100 % 10
    v4 = v // 1000 % 10
    v5 = v // 10000 % 10
    if v1 == v5 and v2 == v4:
        count += 1
print(count)
