#097
# 1 <= a,b,c <= 100
# 1 <= d <= 100

a, b, c, d = map(int, input().split())

AB = abs(a - b)
BC = abs(b - c)
AC = abs(a - c)

if AC <= d:
    print("Yes")
elif AB <= d and BC <= d:
    print("Yes")
else:
    print("No")

