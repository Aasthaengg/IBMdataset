w, a, b = map(int, input().split())
a, b = (a, b) if a < b else (b, a)
if (w + a) > b:
    print(0)
    exit(0)
print(b - (w + a))