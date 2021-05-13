W,a,b=map(int, input().split())
if (a<=b and b<=a+W) or (a>=b and a<=b+W):
    print(0)
else:
    print(max(b-(a+W),a-(b+W)))