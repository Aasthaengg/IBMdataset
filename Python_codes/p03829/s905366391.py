n,a,b = map(int,input().split())
x = list(map(int,input().split()))
ans = 0
now = x[0]
for i in range(n):
    if (x[i] - now)*a >= b:
        ans += b
        now = x[i]
    else:
        ans += (x[i] - now)*a
        now = x[i]
print(ans)