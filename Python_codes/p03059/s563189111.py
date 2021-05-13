a, b, t = map(int, input().split())
if a > t:
    print("0")
else:
    s = t//a
    print(b*s)