n, a, b = map(int, input().split())
li = [a,b]
maxi = min (li)
m = 0
if a + b <= n:
    m = 0
    
if a + b > n:
    m = a + b - n

print(maxi,m)