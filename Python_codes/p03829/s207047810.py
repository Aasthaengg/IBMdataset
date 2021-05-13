n,a,b = map(int,input().split())
x = list(map(int,input().split()))

ans = 0
now = x[0]
for i in range(1,n):
    diff = x[i]-now
    if diff*a > b:
        ans += b
    else:
        ans += diff*a
    now = x[i]
    # print(ans)

print(ans)