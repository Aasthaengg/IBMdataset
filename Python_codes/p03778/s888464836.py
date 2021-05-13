w,a,b = map(int,input().split())
if -1*w <= b - a and b - a <= w:
    print(0)
elif -1*w < b - a:
    print (b-(a+w))
else:
    print (a-(b+w))
