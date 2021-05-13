r, c = map(int, raw_input().split())
m = []
ans = []
for i in range(r):
    a = map(int, raw_input().split())
    m.append(a)
    sum = 0
    for j in range(c):
        print(a[j]),
        sum += a[j]
    print(sum)
total = 0
for i in range(c):
    sum = 0
    for j in range(r):
        sum += m[j][i]
    print(sum),
    total += sum
print(total)