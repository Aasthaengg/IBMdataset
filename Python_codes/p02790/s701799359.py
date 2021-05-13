a, b = map(int, input().split())

if a <= b:
    ans = ""
    for i in range(b):
        ans += str(a)
    print(ans)
else:
    ans = ""
    for i in range(a):
        ans += str(b)
    print(ans)
