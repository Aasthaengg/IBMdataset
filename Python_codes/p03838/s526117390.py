def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

x,y = iim()
if y>=x:
    if x*y>=0:
        ans = y-x
    else:
        ans = abs(x+y)+1
else:
    if y == 0:
        ans = x+1
    elif x*y>0:
        ans = x-y+2
    else:
        ans = abs(y+x)+1
print(ans)
