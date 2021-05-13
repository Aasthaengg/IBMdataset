x,y = map(int,input().split())
ans = 0
if x*y < 0:
    ans += 1
elif (x>0 and y==0) or (x==0 and y<0):
    ans += 1
elif y < x:
    ans += 2
ans += abs(abs(x)-abs(y))
print(ans)