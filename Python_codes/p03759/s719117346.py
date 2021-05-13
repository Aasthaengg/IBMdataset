a, b, c = map(int, input().split())

s = b - a
t = c - b

if s == t:
    print("YES")
else:
    print("NO")