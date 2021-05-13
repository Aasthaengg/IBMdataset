x1,y1,x2,y2 = map(int,input().split())
diffy = x2-x1
diffx = y2-y1
#print(diffy,diffx)
print(x2-diffx,y2+diffy,x1-diffx,y1+diffy)