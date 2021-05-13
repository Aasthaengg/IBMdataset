x,y = map(int,input().split())
if 0<=x<=y:
    a = y-x
elif 0<=y<=x:
    if y>0:
        a = x-y+2
    else:
        a = x-y+1
elif 0>=x>=y:
    if x<0:
        a = x-y+2
    else:
        a = x-y+1
elif 0>=y>=x:
    a = y-x
elif y>=0>=x and abs(x)<=abs(y):
    a = min(y-x,y+x+1)
elif y>=0>=x and abs(x)>abs(y):
    a = min(y-x,-y-x+1)
elif x>=0>=y and abs(x)>=abs(y):
    a = y+x+1
elif x>=0>=y and abs(x)<abs(y):
    a = -y-x+1
print(a)