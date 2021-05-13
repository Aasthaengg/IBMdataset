s = input().split()
a, b = int(s[0]), int(s[1])
if a + b >= 24:
    print(abs(24 - (a + b)))
else:
    print(a + b)