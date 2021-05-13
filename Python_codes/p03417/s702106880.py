n,m = map(int,input().split())

if n == m == 1:
    ans = 1
    
elif min(n,m) == 1 and max(n,m) == 2:
    ans = 0
    
elif min(n,m) == 1 and max(n,m) > 2:
    ans = max(n,m) - 2
    
else:
    ans = (n-2) * (m-2)
    
print(ans)