a, b, x = map(int, input().split())
if a > x:
    print("NO")
    exit()
if a+b >= x: print("YES")
else: print("NO")