W,a,b = map(int, input().split())
if b<=a+W<=b+W or a<=b+W<=a+W:
    print(0)
else:
    print(min(abs(a-b),abs(a+W-b), abs(b+W-a)))