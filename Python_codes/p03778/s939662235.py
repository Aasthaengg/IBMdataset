w,a,b = map(int,input().split())
if b < a:
    temp = a
    a = b
    b = temp
if b >= a + w:
    print(b - a -w)
else:
    print(0)
