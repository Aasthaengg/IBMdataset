w,a,b=map(int,input().split())
if a+w<b:
            print(b-(a+w))
elif a>b+w:
            print(a-(b+w))
elif a+w==b:
            print(0)
elif a<b<a+w<b+w:
            print(0)
elif a==b:
            print(0)
elif b<a<b+w<a+w:
            print(0)
else:
            print(0)
