a, b, t = map(int, input().split())
if t < a:
    print(0)
else:
    print(t // a * b) 