n,m = map(int,input().split())
a = list(map(int,input().split()))
freeday = 0
needday = 0

for i in range(m):
    needday += a[i]
    if needday > n:
        freeday = -1
        break
else:
    freeday = n - needday

print(freeday)
    
