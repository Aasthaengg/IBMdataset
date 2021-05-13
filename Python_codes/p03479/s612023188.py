x, y = map(int, input().split())
cnt = 1
while x < y:
    x *= 2
    cnt += 1
if x == y:
    print(cnt)
else:
    print(cnt-1)