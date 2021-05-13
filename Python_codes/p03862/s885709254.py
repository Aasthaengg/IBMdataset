n,x = map(int,input().split())
a = list(map(int,input().split()))

count = 0

for i in range(n-1):
    if a[i] > x:
        count += a[i] - x
        a[i] = x
        
        count += a[i+1]
        a[i+1] = 0
        
    elif a[i]+a[i+1] > x:
        count = count + a[i+1] + a[i] - x
        a[i+1] = x - a[i] 
    
print(count)
