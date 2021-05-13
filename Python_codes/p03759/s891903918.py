a, b, c = map(int, input().split())

d1 = b - a
d2 = c - b

if (d1 == d2):
    print("YES")

else:
    print("NO")