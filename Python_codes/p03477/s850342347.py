a,b,c,d = map(int, input().split())

ans = "Balanced"
if a+b > c+d: ans = "Left"
elif a+b < c+d: ans = "Right"
print(ans)