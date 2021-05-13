n = int(input())
a = list(map(int,input().split()))

point = 0
point2 = 0

now = 0
now2 = 0

for i,j in enumerate(a):
    now += j
    now2 += j
    if i%2 == 0:
        if now <= 0:
            point += 1-now
            now = 1
        if now2 >= 0:
            point2 += 1+now2
            now2 = -1
    else:
        if now2 <= 0:
            point2 += 1-now2
            now2 = 1
        if now >= 0:
            point += 1+now
            now = -1

print(min(point,point2))