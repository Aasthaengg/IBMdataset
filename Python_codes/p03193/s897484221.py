N, H, W = map(int, input().split(" "))
x, y = list(), list()
for i in range(N) :
    _x, _y = input().split(" ")
    x.append(int(_x))
    y.append(int(_y))
    
cnt = 0
for _x, _y in zip(x, y) :
    if _x >= H and _y >= W : cnt += 1
        
print(cnt)