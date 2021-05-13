w,a,b = map(int, input().split())
ans = 0
if a < b: ans = b-a-w
else: ans = a-b-w
print(0 if  ans < 0 else ans)