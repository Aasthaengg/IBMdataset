a, b, x = [int(i) for i in input().split()]

if 0 <= (x - a) <= b:
    print("YES")
else:
    print("NO")
