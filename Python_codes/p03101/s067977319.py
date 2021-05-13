H, W = map(int, input().split())
h, w = map(int, input().split())

ans = H * W
ans -= h * W  +  ((H - h) * w)
print(ans)