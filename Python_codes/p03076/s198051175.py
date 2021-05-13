a = []
for _ in range(5):
    a.append(int(input()))
res = 0
last_num = a[0]
for i in range(5):
    if a[i] % 10 == 0:
        res += a[i]
    else:
        if last_num % 10 == 0:
            last_num = a[i]
        elif a[i] % 10 < last_num % 10:
            last_num = a[i]
        res += (a[i] // 10 + 1) * 10

if last_num % 10 != 0:
    res -= 10 - last_num % 10
print(res)
