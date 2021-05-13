a, b, x = list(map(int, input().split()))

if x - a >= 0 and x - a <= b:
    print("YES")
else:
    print("NO")