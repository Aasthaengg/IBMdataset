n=int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
max_h = 0
max_x = 0
max_y = 0
for p,q,h in xy:
    if max_h < h:
        max_h = h
        max_x = p
        max_y = q

for top_x in range(101):
    for top_y in range(101):
        top_h = abs(max_x-top_x)+abs(max_y-top_y)+max_h
        for x,y,h in xy:
            if max(top_h-abs(top_x-x)-abs(top_y-y),0) != h:
                break
        else:
            print(top_x,top_y,top_h)
            exit()

