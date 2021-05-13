x = int(input())
cnt = 0
if x>11:
    cnt += 2*(x//11)
    x %= 11

while True:
    if x<=0:
        break
    x -= 6
    cnt += 1
    if x <= 0:
        break
    x -= 5
    cnt += 1
    if x<=0:
        break
print(cnt)