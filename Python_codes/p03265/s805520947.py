a,b,c,d=map(int,input().split())
x = abs(a-c)
y = abs(b-d)
if b <= d:
    ax = c - y
    bx = a - y
else:
    ax = c + y
    bx = a + y
if a <= c:
    ay = d + x
    by = b + x
else:
    ay = d - x
    by = b - x
print(str(ax)+' '+str(ay)+' '+str(bx)+' '+str(by))