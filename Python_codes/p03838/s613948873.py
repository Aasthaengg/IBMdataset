x,y = map(int,input().split())

cnt = abs(abs(x) - abs(y))
if abs(x) < abs(y): 
    if x >= 0 and y >= 0: print(cnt)
    elif x < 0 and y < 0: print(cnt+2)
    else: print(cnt+1)
elif abs(x) > abs(y):
    if x >=0 and y > 0: print(cnt+2)
    elif x < 0 and y <= 0: print(cnt) 
    else: print(cnt+1)
elif abs(x) == abs(y):
    if x*y >= 0:print(cnt)
    else: print(cnt+1)