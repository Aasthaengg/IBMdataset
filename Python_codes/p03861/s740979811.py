a,b,x = map(int,input().split())

up = b//x*x
if a%x == 0:
    down = a
else:
    down = (a//x+1)*x
ans = (up-down)//x+1
print(ans)