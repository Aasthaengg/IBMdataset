X = int(input())
cur = X
cnt = 1
while cur % 360:
    cur += X
    cur %= 360
    cnt += 1
print(cnt)
