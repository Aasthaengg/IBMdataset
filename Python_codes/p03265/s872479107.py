x1,y1,x2,y2=list(map(int,input().split()))

if x2>=x1 and y2>=y1:
  x3=x2-abs(y2-y1);y3=y2+abs(x2-x1);x4=x3-abs(y3-y2);y4=y3-abs(x3-x2)

elif x2<=x1 and y2>=y1:
  x3=x2-abs(y2-y1);y3=y2-abs(x2-x1);x4=x3+abs(y3-y2);y4=y3-abs(x3-x2)

elif x2<=x1 and y2<=y1:
  x3=x2+abs(y2-y1);y3=y2-abs(x2-x1);x4=x3+abs(y3-y2);y4=y3+abs(x3-x2)

elif x2>=x1 and y2<=y1:
  x3=x2+abs(y2-y1);y3=y2+abs(x2-x1);x4=x3-abs(y3-y2);y4=y3+abs(x3-x2)

  
print(x3,y3,x4,y4)
