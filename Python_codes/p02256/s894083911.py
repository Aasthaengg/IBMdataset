s = input()
x,y = map(int,s.split())

while(x != y or x>1 or y > 1):
    if(x < y):
        tmp = x
        x = y
        y = tmp
    if( y == 0):
        break

    x %= y
print(x)