x1,y1,x2,y2 = map(int, input().split())
x_dis = x2-x1
y_dis = y2-y1
print(x2-y_dis,y2+x_dis,x1-y_dis,y1+x_dis)