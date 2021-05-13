a, b, c = map(int, input().split())
if a - b < 0:
    print(c)
elif c-(a-b) < 0:
    print(0)
else:
    print(c-(a-b))
