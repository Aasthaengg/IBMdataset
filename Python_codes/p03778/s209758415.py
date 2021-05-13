w, a, b = map(int, input().split())

if a <= b <= a+w or b <= a <= b+w:
    print(0)
    exit()
if a < b:
    x = b - (a + w)
    print(x)
elif a > b:
    x = a - (b + w)
    print(x)