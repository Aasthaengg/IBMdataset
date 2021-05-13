n,x,t = map(int,input().split())
c  = 0 
ans = 0
while n > c:
    c += x
    ans += t
print(ans)
