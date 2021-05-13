n = 5
t = [int(input()) for _ in range(n)]

last, min = 0, 9
for i in range(n):
    if t[i] % 10 < min:
        if t[i] % 10 == 0:
            continue
        last = i
        min = t[i] % 10

ans = 0
for i in range(n):
    if i == last:
        continue
    if t[i] % 10 == 0:
        diff = 0
    else:
        diff = 10 - t[i] % 10
    ans += t[i] + diff

ans += t[last]

print(ans)