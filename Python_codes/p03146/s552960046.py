s = int(input())

if s == 1 or s == 2:
    print(4)
    exit()

ans = 1
while s != 4:
    ans += 1
    if s % 2 == 0:
        s //= 2
    else:
        s *= 3
        s += 1

print(ans + 3)