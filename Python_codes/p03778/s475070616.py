w,a,b=map(int,input().split())
if b<=a+w<=b+w or b<=a<=b+w:
    print("0")
else:
    if a+w<b:
        print(b-a-w)
    elif b+w<a:
        print(a-b-w)
