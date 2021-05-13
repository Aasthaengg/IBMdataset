x = int(input())
xm = x // 11
if x % 11 > 6:
    print(xm*2 + 2)
elif x % 11 == 0:
    print(xm*2)
else:
    print(xm*2 + 1)
