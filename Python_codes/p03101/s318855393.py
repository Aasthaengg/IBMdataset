H, W = (int(x) for x in input().split())
h, w = (int(x) for x in input().split())


ans=H*W-(h*W+(H-h)*w)
print(ans)
