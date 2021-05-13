n, a, b = map(int, input().split(" "))
sum = 0
for e in range(a, n + 1):
    c = 0
    ee = e
    while True:
        c += e % 10
        e = e // 10
        if e == 0:
            break
    if a <= c <= b:
        sum += ee
print(sum)