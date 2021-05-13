n,m = map(int, input().split())

if n*2 <= m:
    ma = m-n*2
    ans = n+(ma//4)
    
else:
    ans = m//2

print(ans)