#coding: UTF-8

n = int(input())
point_t = 0
point_h = 0

for i in range(n):
    cards = list(map(str, input().split()))
    taro = cards[0]
    hanako = cards[1]
    if taro < hanako:
        point_h += 3
    elif taro > hanako:
        point_t += 3
    else:
        point_t += 1
        point_h += 1

print(point_t, point_h)
