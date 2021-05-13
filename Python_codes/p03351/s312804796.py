a, s, d, f = map(int, input().split())
if abs(d - s) <= f and abs(s - a) <= f or abs(d - a) <= f:
    print("Yes")
else:
    print("No")
