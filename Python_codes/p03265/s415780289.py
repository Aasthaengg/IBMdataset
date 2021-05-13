x,y,xx,yy = map(int,open(0).read().split())
print(xx-(yy-y), yy+(xx-x), x-(yy-y), y+(xx-x))