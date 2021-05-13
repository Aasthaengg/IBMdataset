a, b = map(int, input().split())

if b >= a:
    print(a)
elif a > b:
    print(a-1)
else:
    print(b)