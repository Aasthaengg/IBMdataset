w, a, b = map(int, input().split())

if b <= a+w <= b+w:
    print(0)
else:
    print(min(abs(a+w-b), abs(a-b-w)))
