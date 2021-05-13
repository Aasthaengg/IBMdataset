w, a, b = map(int, input().split())
if a <= b and b <= a+w:
    print(0)
elif b <= a+w and a <= b:
    print(0)
else:
    print(min(abs(a-b-w), abs(a+w-b)))