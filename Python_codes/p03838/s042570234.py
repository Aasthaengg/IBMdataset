import sys
input = sys.stdin.readline

x,y = list(map(int,input().split()))
dxy = abs(abs(x)-abs(y))
if y-x == -1 * dxy:
    ans = dxy+2
    if x == 0 or y ==0:
        ans -=1    
elif y-x == dxy:
    ans = dxy
else:
    ans = dxy+1
    
print(ans)
