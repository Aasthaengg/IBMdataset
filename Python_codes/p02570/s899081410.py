d,t,s = map(int,input().split())
ans = "No"

if s * t >= d:
    ans = "Yes"
    
print(ans)