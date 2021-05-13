x,y = map(int,input().split())
print(abs(abs(x)-abs(y)) + int(x>y)*(abs(int(x*y>0))+1) + int(x<y)*(abs(int(x*y<0))))