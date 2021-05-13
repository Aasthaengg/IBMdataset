a, b, c, d = map(int, input().split())

ab = a*b
cd = c*d
if ab>cd:print(ab)
elif cd>ab:print(cd)
else:print(ab)