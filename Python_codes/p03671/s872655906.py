a, b, c = map(int, input().split())

ans = max(a, b, c)

if ans == a:
    print(b+c)
elif ans == b:
    print(a+c)
elif ans == c:
    print(a+b)