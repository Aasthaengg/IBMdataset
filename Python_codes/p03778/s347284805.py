W,a,b = list(map(int,input().split()))
if (a<=b<=a+W) or (a<=b+W<=a+W) or (b<=a<=b+W) or (b<=a+W<=b+W):
    c=0
else:
    c = min(abs(b-a-W),abs(a-b-W))
print(c)
