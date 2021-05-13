x,a,b = map(int, input().split())
dist_a = abs(x-a)
dist_b = abs(x-b)
if dist_a > dist_b:
    print("B")
else:
    print("A")