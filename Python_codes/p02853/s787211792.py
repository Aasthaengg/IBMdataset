x,y = map(int,input().split())
c = 0
if x==1:
    c+=300000
elif x == 2:
    c+=200000
elif x == 3:
    c+=100000
    
if y==1:
    c+=300000
elif y == 2:
    c+=200000
elif y == 3:
    c+=100000

if x == 1 and y == 1:
    c+=400000
    
print(c)