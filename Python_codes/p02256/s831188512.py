x, y = map(int, input().split())

if x > y :
    pass
else :
    x, y = y, x

while x % y != 0 :
    d = x % y
    x = y
    y = d
print(y)    
