a, b, c = map(int, input().split())
if b-(a*c) > 0:
    print(c)
elif (b//a) > c:
    print(c)
else:
    print(b//a)
