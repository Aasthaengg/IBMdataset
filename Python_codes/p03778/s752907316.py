w, a, b = map(int, input().split())

if a <= b <= a + w or b <= a <= b + w:
    print(0)
else:
    print(abs(b - a) - w)
