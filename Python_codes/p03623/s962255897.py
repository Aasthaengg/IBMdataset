x,a,b = map(int,input().split())
s = abs(a - x)
t = abs(b - x)
ans = "A"
if s > t:
    ans = "B"

print(ans)
