n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
a.sort()
b.sort()
c.sort()
ans = 0
for j in range(n):
    bind = j
    top = n
    bot = -1
    while top-bot > 1:
        mid = (top+bot)//2
        if b[bind] > a[mid]:bot = mid
        else:top = mid
    
    aind = bot
    l = -1
    r = n
   
    while r-l> 1:
   
        cen = (l+r)//2
        if b[bind] < c[cen]:r = cen
        else:l = cen
    cind = r
    ans +=(aind+1)*(n-cind)
    
print(ans)
    
