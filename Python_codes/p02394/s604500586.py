w, h, x, y, r = map(int, input().split())

if (x >= -100 and x <= 100) and (y >= -100 and y <= 100):
    if (w > 0 and w <= 100) and (h > 0 and h <= 100) and (r > 0 and r <= 100):
        
        if x > w:
            print("No")
        elif y > h:
            print("No")
        elif x < 0:
            print("No")
        elif y < 0:
            print("No")
        elif (x + r) > w:
            print("No")
        elif (y + r) > h:
            print("No")
        elif x < r:
            print("No")
        elif y < r:
            print("No")
        else:
            print("Yes")