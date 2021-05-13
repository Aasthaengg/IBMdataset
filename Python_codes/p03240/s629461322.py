from sys import exit

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

for cx in range(101):
    for cy in range(101):
        correct_flag = True
        for i in range(n):
            x, y, h = l[i]
            if h > 0:
                res_h = abs(x - cx) + abs(y - cy) + h
                break
        for i in range(n):
            x, y, h = l[i]
            if max(res_h - abs(x - cx) - abs(y - cy), 0) != h:
                correct_flag = False
                break
        if correct_flag:
            print(cx, cy, res_h)
            exit()