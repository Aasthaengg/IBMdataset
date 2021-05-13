W, a, b = map(int, input().split())
if b>a+W:
    print(b-a-W)
elif a+W>=b>=a:
    print(0)
elif a>b:
    print(a-b-W)