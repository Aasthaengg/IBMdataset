# ABC127
# A Ferris Wheel
a, b = map(int, input().split())
if a > 12:
    print(b)
    exit()
elif a < 6:
    print(0)
    exit()
else:
    print(b // 2)
    exit()
