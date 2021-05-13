def first(x):
    cnt = 0
    for i in range(1, h+1):
        for j in range(1, x+1):
            if kv[i][j] == 0:
                kv[i][j] = 1
                cnt += 1
    return cnt

def second(x):
    cnt = 0
    for i in range(1, h+1):
        for j in range(x+1, w+1):
            if kv[i][j] == 0:
                kv[i][j] = 1
                cnt += 1
    return cnt

def fourth(y):
    global kv
    cnt = 0
    for i in range(y+1, h+1):
        for j in range(1, w+1):
            if kv[i][j] == 0:
                kv[i][j] = 1
                cnt += 1
    return cnt

def third(y):
    cnt = 0
    for i in range(y, 0, -1):
        for j in range(1, w+1):
            if kv[i][j] == 0:
                kv[i][j] = 1
                cnt += 1
    return cnt


w, h, n = map(int, input().split())

kv = [[0 for _ in range(w+1)] for _ in range(h+1)]
whites = w * h
blacks = 0


for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        blacks += first(x)
    elif a == 2:
        blacks += second(x)
    elif a == 3:
        blacks += third(y)
    elif a== 4:
        blacks += fourth(y)
print(whites-blacks)
