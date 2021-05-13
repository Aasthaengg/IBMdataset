a, b, t = map(int, input().split())
if a > t:
    print(0)
else:
    ans = b * ((t+0.5)//a)
    print(int(ans))