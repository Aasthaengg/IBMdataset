x, y = map(int, input().split())
ans = 10**9 + 10
if x == y:
    ans = 0
else:
    #1
    ans1 = y-x
    ans2 = (-y)-(-x) + 2
    ans3 = y-(-x) + 1
    ans4 = (-y)-x + 1
    if ans1 > 0:
        ans = min(ans, ans1)
    if ans2 > 0:
        ans = min(ans, ans2)
    if ans3 > 0:
        ans = min(ans, ans3)
    if ans4 > 0:
        ans = min(ans, ans4)

print(ans)
