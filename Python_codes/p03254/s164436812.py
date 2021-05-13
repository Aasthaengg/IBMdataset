N, x = map(int, input().split())
a = sorted(list(map(int, input().split())))
cnt = 0
for i in a:
    if x >= i:
        cnt += 1
        x -= i
    else:
        x = 0
        break
if x > 0:
    cnt -= 1
print(cnt)