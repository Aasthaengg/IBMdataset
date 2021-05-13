x,y = map(int,input().split())
ans = 0
if x == 1 and y == 1:
    ans += 400000

def q(x,ans):
    if x == 1:
        ans += 300000
    elif x == 2:
        ans += 200000
    elif x == 3:
        ans += 100000
    return ans
ans = q(x,ans)
ans = q(y,ans)
print(ans)