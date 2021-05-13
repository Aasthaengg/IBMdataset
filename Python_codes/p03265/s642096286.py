x1,y1,x2,y2 = map(int,input().split())
 
side_x=x2-x1
side_y=y2-y1
 
pattern = [[side_x,side_y],[-side_y,side_x],[-side_x,-side_y],[side_y,side_x]]*2
 
i = pattern.index([side_x,side_y])
x3,y3 = x2+pattern[i+1][0],y2+pattern[i+1][1]
x4,y4 = x3+pattern[i+2][0],y3+pattern[i+2][1]
print(x3,y3,x4,y4)