a, b, c, d = map(int, input().split())
m = abs(a-b)
n = abs(b-c)
l = abs(a-c)
if l > 2 * d:
    print("No")
elif l <= d:
    print("Yes")
else:
    if m <= d and n <= d:
        print("Yes")
    else:
        print("No")
