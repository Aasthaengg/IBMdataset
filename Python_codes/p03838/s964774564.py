x, y = list(map(int, input().split()))
ans = 0
def sign(x):
    return (x > 0) - (x < 0)
if sign(x)==sign(y):
    if x<y:
        ans = abs(x-y)
    else:
        ans = abs(x-y) + 2
elif x and y:
    if abs(x)!=abs(y):
        ans = abs(abs(x)-abs(y)) + 1
    else:
        ans = 1
else:
    if x==0:
        if sign(y)==-1:
            ans = abs(y) + 1
        elif sign(y)==1:
            ans = abs(y)
    elif y==0:
        if sign(x)==-1:
            ans = abs(x)
        elif sign(x)==1:
            ans = abs(x) + 1




print(ans)