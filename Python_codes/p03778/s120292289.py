W,a,b = map(int, input().split())

if (a <= b <= a+W) or (a <= b+W <= a+W):
    print(0)
else:
    if a+W < b:
        print(abs(b-(a+W)))
    elif b+W < a:
        print(abs(a-(b+W)))