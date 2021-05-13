n,x = map(int,input().split())
a = list(map(int,input().split()))
tmp = [0]*n
tmp[0] = a[0] if a[0] < x else x
val = a[0]
for i in range(n-1):
    if a[i+1] + val > x:
        tmp[i+1] = max(0,x-val)
    else:tmp[i+1] = a[i+1]
    val = tmp[i+1]

ans = 0
for i in range(n):
    ans += a[i] - tmp[i]
print(ans)

        
    
