a,b,c,k = map(int,input().split())
ans = b - a

if k % 2 == 0:
    ans = a - b
    
print(ans)