x,y=input().split()
l=['1','3','5','7','8','10','12','4','6','9','11','2']
x_loc=l.index(x)
y_loc=l.index(y)

if x_loc==11 and y_loc==11:
    print('Yes')
elif x_loc<7 and y_loc<7:
    print('Yes')
elif x_loc>6 and x_loc<11 and y_loc>6 and y_loc<11:
    print('Yes')
else:
    print('No')