x = int(input())

ans = 0
tmp = 0
while True:
    ans += 1
    tmp += x
    if tmp % 360 == 0:
        break
print(ans)
