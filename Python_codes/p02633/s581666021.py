n = int(input())
res = 1
while True:
    if (res * n) % 360 == 0:
        break
    res += 1
print(res)
