a,b,c,d = map(int, input().split())
x = abs(a - b)
y = abs(b - c)
z = abs(a - c)
if x <= d and y <= d or z <= d:
    print("Yes")
else:
    print("No")