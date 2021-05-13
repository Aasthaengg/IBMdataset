w, a, b = map(int, input().split())

if b + w < a:
    print(a - (b + w))
elif a <= b + w <= a + w:
    print(0)
elif a <= b <= a + w:
    print(0)
elif a + w < b:
    print(b - (a + w))