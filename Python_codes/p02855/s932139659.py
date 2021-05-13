h,w,k = map(int,input().split())

s = [input() for _ in range(h)]

t = [[0 for _ in range(w)] for _ in range(h)]

i = 1

for y in range(h):
    for x in range(w):
        if(s[y][x] == '#'):
            t[y][x] = i
            i += 1

for y in range(h):
    l = 0
    for x in range(w):
        if(t[y][x] != 0):l = t[y][x]
        else:t[y][x] = l
    l = 0
    for x in range(w)[::-1]:
        if(t[y][x] != 0):l = t[y][x]
        else:t[y][x] = l

for y in range(h):
    if(t[y][0] == 0):
        for y2 in range(y,h):
            if(t[y2][0] == 0):continue
            for x in range(w):
                t[y][x] = t[y2][x]
            break
                
for y in range(h)[::-1]:
    if(t[y][0] == 0):
        for y2 in range(0,y)[::-1]:
            if(t[y2][0] == 0):continue
            for x in range(w):
                t[y][x] = t[y2][x]
            break


for x in t:print(*x)
