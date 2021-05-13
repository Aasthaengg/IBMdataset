W, H, x, y = map(int, input().split())

ans0 = float(W * H) / 2

ans1 = 0
if W%2 == 0 and H%2 == 0 and W//2 == x and H//2 == y:
    ans1 = 1
    
print(ans0, ans1)
