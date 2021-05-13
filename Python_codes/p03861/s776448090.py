a, b, x = map(int, input().split())
fb = b//x + 1
if a == 0:
    fam = 0
else:
    fam = (a-1)//x + 1
print(fb-fam)