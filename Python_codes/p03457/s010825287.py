n = int(input())
 
ti,xi,yi = 0,0,0
found = True
for _ in range(n):
    t, x, y = map(int, input().split())
    root = abs(x-xi)+abs(y-yi)
    if root > (t-ti) or (t-ti-root)&1:
        found = False
    ti,xi,yi = t,x,y  
    
print("Yes" if found else "No")