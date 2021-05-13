# input
W, H, x, y = map(int, input().split())

# check
ans = (W * H) / 2

if W % 2 == 0 and H % 2 == 0 and W // 2 == x and H // 2 == y:
    print(ans, 1, sep=" ")
else:
    print(ans, 0, sep=" ")
