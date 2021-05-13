w, a, b = map(int, input().split())
a, b = min(a, b), max(a, b)
if a+w >= b:
    print(0)
else:
    print(b-(a+w))