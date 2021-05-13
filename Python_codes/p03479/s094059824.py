x,y = map(int, input().split())

cnt = 0
a = x
while a <= y:
    a += a
    cnt += 1
print(cnt)