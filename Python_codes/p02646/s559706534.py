a, v = [int(k) for k in input().split()]
b, w = [int(k) for k in input().split()]
t = int(input())
d = abs(a - b)
if d <= v * t - w * t:
    print("YES")
else:
    print("NO")