n, x = map(int, input().split())
a = sorted(list(map(int, input().split())))

cnt = 0
flag = False
for i in a:
    if i <= x:
        x -= i
        cnt += 1
        if x == 0:
            flag = True
    else:
        break
else:
    if not flag:
        cnt -= 1
print(cnt)