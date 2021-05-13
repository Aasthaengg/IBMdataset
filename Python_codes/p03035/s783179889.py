a, b = map(int, input().split())
if a >= 13:
    print(b)
elif 12 >= a >= 6:
    print(int(b/2))
elif 5 >= a:
    print(int(0))