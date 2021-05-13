x = int(input())
if x % 11 > 6:
    print((x//11)*2 + 2)
elif 0 < x % 11 <= 6:
    print((x//11)*2 + 1)
else:
    print((x//11)*2)
