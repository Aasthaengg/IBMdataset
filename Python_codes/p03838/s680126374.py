x,y = map(int,input().split())

res = 10**10
cnt = 0
for mask in range(1<<2):
    _x = x
    _y = y
    if mask & 1:
        _x *= -1
        cnt +=1
    if (mask>>1) & 1:
        _y *= -1
        cnt += 1
    if _x <= _y:
        cnt += _y-_x
        res = min(res,cnt)
    cnt = 0
print(res)