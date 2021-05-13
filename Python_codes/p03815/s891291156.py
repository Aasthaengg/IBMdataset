x = int(input())
cnt = (x // 11)
x -= cnt*11
cnt *= 2
if x > 0:
    if x > 6:
        cnt += 2
    else:
        cnt += 1
print(cnt)