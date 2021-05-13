a, b, x = (int(x) for x in input().split())
if a > x or a+b < x:
    print("NO")
else:
    print("YES")