w, a, b = map(int, input().split())

if w >= abs(a-b):
    print(0)
else:
    if a > b:
        print(a-(b+w))
    else:
        print(b-(a+w))