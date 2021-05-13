import math

a, b, n = map(int, input().split())

if n+1 >= b:
    x = b
else:
    x = n

ans = [math.floor(a*x/b) - a*math.floor(x/b)]
ans.append(math.floor(a*(x-1)/b) - a*math.floor((x-1)/b))
if x < n:
    ans.append(math.floor(a*(x+1)/b) - a*math.floor((x+1)/b))

print(max(ans))