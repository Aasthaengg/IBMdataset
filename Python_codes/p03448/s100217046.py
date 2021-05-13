a, b, c, x = int(input()), int(input()), int(input()), int(input())

res = 0
for i in range(a+1):
    rem = x
    rem -= 500 * i
    tempA = rem
    if rem == 0:
        res += 1
        continue
    for j in range(b+1):
        rem = tempA
        rem -= 100 * j
        tempB = rem
        if rem == 0:
            res += 1
            continue
        for k in range(c+1):
            rem = tempB
            rem -= 50 * k
            if rem == 0:
                res += 1
                break

print(res)