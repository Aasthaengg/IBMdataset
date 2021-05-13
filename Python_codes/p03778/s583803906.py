W, a, b = map(int,input().split())
if b > a+W:
    print(abs(b-(a+W)))
elif b <= a+W and b+W >= a:
    print(0)
else:
    print(abs(b+W-a))