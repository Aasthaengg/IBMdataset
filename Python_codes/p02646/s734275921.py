a, v = [int(x) for x in input().split()]
b, w = [int(x) for x in input().split()]
t = int(input())
if w > v:
    print("NO")
elif w == v:
    if a == b:
        print("YES")
    else:
        print("NO")
else:
    if abs(a - b)/(v - w) <= t:
        print("YES")
    else:
        print("NO")
