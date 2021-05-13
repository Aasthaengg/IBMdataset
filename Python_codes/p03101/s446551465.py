h, w = map(int, input().split())
sh, sw = map(int, input().split())
ans = (h - sh) * (w - sw)
print(ans)