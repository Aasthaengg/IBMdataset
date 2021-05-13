
x1, y1, x2, y2= map(float, input().split())

apple = ((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))**0.5

print('{:.5f}'.format(apple))
