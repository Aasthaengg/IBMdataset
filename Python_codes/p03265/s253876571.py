x1,y1,x2,y2 = map(int,input().split())
print(str(x2-(y2-y1)) + " " + str(y2-(x1-x2)) + " " + str(x1-(y2-y1)) + " " + str(y1-(x1-x2)))