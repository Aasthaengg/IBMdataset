w, a, b = map(int,input().split())
a, b = sorted([a, b])
a += w
if a < b:
    print(b-a)
else:
    print(0)