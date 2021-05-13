x, y = map(int,input().split())

cnt = 1
while True:
    x = x * 2
    if x > y:
        break
    cnt += 1
print(cnt)