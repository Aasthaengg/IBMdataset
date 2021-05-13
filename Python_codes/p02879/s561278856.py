a, b = map(int, input().split())
x = a * b

if len(str(a)) < 2:
    if len(str(b)) < 2:
        print(x)
        exit()
print(-1)
