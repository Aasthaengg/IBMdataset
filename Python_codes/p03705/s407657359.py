n, a, b = map(int, input().split())
if n == 1:
    if a == b:
        print(1)
    else:
        print(0)
elif b < a:
    print(0)
else:
    print(b*(n-1)+a-a*(n-1)-b+1)