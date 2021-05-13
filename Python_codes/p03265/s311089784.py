x1,y1,x2,y2 = map(int, input().split())
print(str(x2+y1-y2) + " " + str(y2+x2-x1) + " " + str(x1+y1-y2)+ " " + str(y1+x2-x1))