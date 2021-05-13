x1,y1,x2,y2 = list(map(int,input().split()))
vectorX = x2 - x1
vectorY = y2 - y1
x3 = x2 - vectorY
y3 = y2 + vectorX
x4 = x3 - vectorX
y4 = y3 - vectorY
answer = str(x3) + " " + str(y3) + " " + str(x4) + " " + str(y4)
print(answer)