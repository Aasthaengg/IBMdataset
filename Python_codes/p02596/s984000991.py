k = int(input())
if k % 2 == 0 or k % 5 == 0:
    print(-1)
    exit()
cnt, yep = 0, 0
while True:
    yep = (yep * 10 + 7) % k
    cnt += 1
    if yep == 0:
        break
print(cnt)