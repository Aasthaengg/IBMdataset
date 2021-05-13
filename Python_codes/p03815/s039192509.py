x = int(input())
e = x // 11
d = x - e * 11

if d > 6:
    print(e*2 + 2)
elif 0 < d <= 6:
    print(e*2 + 1)
else:
    print(e*2)
