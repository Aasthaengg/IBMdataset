"""
tuple
"""
n,Y = map(int,input().split())
ans = -1,-1,-1
for x in range(n+1):
    for y in range(n-x+1):
        z = n - x - y 
        if 0 <= z <=2000 and (10000*x+5000*y+z*1000)==Y:
            ans = x,y,z
            break
        else :
            continue
        break
print(*ans)

