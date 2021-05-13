x,y,X,Y=map(int,input().split())
keyx=X-x
keyy=Y-y
xx=X-keyy
XX=xx-keyx
yy=Y+keyx
YY=yy-keyy
print(xx,yy,XX,YY)