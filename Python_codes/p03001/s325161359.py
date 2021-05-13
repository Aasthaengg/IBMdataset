W, H, x, y = map(int, input().split())
mid = [W/2, H/2]
ans1 = W*H/2
if mid[0] == x and mid[1] == y:
    ans2 = 1
else:
    ans2 = 0
print(ans1, ans2)