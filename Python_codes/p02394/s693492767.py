W, H, x, y, r = [int(i) for i in input().split()]
ans = "Yes"
if x - r < 0 or W < x + r: ans = "No"
if y - r < 0 or H < y + r: ans = "No"
print(ans)