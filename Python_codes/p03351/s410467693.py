a, b, c, d = [int(i) for i in input().split()]

ab = abs(a - b) <= d
ac = abs(a - c) <= d
bc = abs(b - c) <= d

if ac or (ab and bc):
    print("Yes")
else:
    print("No")