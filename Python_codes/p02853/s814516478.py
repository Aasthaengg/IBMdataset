x,y = map(int,input().split())
ans = 0
if x<= 3:
    ans += 400000-100000*x
if y <= 3:
    ans += 400000-100000*y
if x== 1 and y == 1:
    ans += 400000
print(ans)