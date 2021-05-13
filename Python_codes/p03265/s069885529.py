# ABC108B

x1, y1, x2, y2 = map(int, input().split())
if x1 <= x2 and y1 <= y2:
    d4 = x2-x1
    d3 = y2-y1
    print(x2-d3, y2+d4, x1-d3, y1+d4)
elif x1 > x2 and y1 <= y2:
    d4 = y2-y1
    d3 = x1-x2
    print(x2-d4, y2-d3, x1-d4, y1-d3)
elif x1 > x2 and y1 > y2:
    d4 = x1-x2
    d3 = y1-y2
    print(x2+d3, y2-d4, x1+d3, y1-d4)
elif x1 <= x2 and y1  > y2:
    d4 = y1-y2
    d3 = x2-x1
    print(x2+d4, y2+d3, x1+d4, y1+d3)
