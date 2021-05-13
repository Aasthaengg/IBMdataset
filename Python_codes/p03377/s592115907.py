a, b, c = list(map(int, input().split()))
 
d = c - a

ans = "NO"

if d>=0:
    if d <= b:
        ans = "YES"
else:
    ans = "NO"
    
print(ans)