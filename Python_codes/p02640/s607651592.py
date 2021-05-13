x,y= map(int, input().split())
#条件が成り立つか判断
turu = 2*x - 0.5*y
kame = x - turu

if  turu >= 0 and kame >= 0 and y % 2 == 0 :
    print('Yes')
else :
    print('No')