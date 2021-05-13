a,b,c = map(int,input().split())
s = [a,b,c]
ans = 0

while a%2 + b%2 + c%2 == 0:
    na = (b + c) // 2
    nb = (a + c) // 2
    nc = (a + b) // 2
    
    if [na,nb,nc] == s:
        ans = -1
        break
        
    else:
        a = na
        b = nb
        c = nc
        ans += 1
        
print(ans)