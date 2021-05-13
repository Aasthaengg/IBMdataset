(*c, ) = map(int, open(0).read().split())
print("YNeos"[sum(c) % 3 > 0 or sum(c)//3 != c[0]+c[4]+c[8]::2])
