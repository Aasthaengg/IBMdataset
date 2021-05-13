r,d,x = list(map(int,input().split()))

ans =x*r-d
for i in range(10):
    print(ans)
    ans = ans*r-d