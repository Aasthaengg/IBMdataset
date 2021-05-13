a, b, c, d = [int(x) for x in input().split()]
l, r = a + b, c + d
ans = "Balanced"
if l > r:
    ans = "Left"
elif l < r:
    ans = "Right"
print(ans)