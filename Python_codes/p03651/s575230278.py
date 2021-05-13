def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)
    
n , k = map(int,input().split())
a = list(map(int,input().split()))
fl = ""

if k > max(a):
    fl = "IMPOSSIBLE"

else:
    g = a[0]
    for i in range(n-1):
        g = gcd( g , a[i+1] )
        
    if k % g == 0:
        fl = "POSSIBLE"
    else:
        fl = "IMPOSSIBLE"
        
print(fl)