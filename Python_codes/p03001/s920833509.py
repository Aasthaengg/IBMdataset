W, H, X, Y = map(int, input().split())

ans1 = (W*H)/2
if W == X*2 and H == Y*2:
    ans2 = 1
else:
    ans2 = 0
print(ans1, ans2)
