x,y = map(int,input().split())
ans = abs(abs(x) - abs(y))
if(x*y>0)&(x>y):
    ans += 2
if(x*y < 0):
    ans += 1
if(x*y==0)&(x>y):
    ans += 1
print(ans)