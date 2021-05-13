n = int(input())
p =list(map(int,input().split()))
ans = 0

if p[-1] == n:
    a = p[-2]
    b = p[-1]
    
    p[-2] = b
    p[-1] = a
    
    ans += 1

for i in range(n-1):
    if i == p[i]-1:
        a = p[i]
        b = p[i+1]
        
        p[i] = b
        p[i+1] = a
        
        ans += 1
        
print(ans)