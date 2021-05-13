a, b, c, d = map(int, input().split())
if a <= 0 and b >= 0:
    print(max(a*c, a*d, b*c, b*d, 0))
elif c <= 0 and d >= 0:
    print(max(a*c, a*d, b*c, b*d, 0))
else :
    print(max(a*c, a*d, b*c, b*d))