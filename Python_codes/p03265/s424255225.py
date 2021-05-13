x1,y1,x2,y2 = map(int,input().split())
vec = [y1-y2,x2-x1]

print(x2+vec[0],y2+vec[1],x1+vec[0],y1+vec[1])