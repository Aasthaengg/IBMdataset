w, h , x ,y ,r = map(int,input().split())

xLongLeft = x-r
xLongRight = x + r

yLongTop = y + r
yLongBot = y - r

if((xLongLeft >= 0 and yLongBot >= 0) and (xLongRight <= w and yLongTop <= h)):
   print('Yes')
else:
   print('No')

