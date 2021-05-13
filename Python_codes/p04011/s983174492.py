n = int(input())
k = int(input())
x = int(input())
y = int(input())

xdays = min(n,k)
ydays = n-xdays

ans = xdays*x + ydays*y
print(ans)