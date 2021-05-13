w, h, x, y = map(int, input().split())

ans  = (w*h)/2

if (x+x) == w and (y+y) == h:
    judge = 1
else:
    judge = 0
    
print(ans, judge)