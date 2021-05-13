w,a,b = map(int,input().split())
a1 = a
a2 = a+w
b1 = b
b2 = b+w
if abs(b-a) > w:
    print(min(abs(b1-a2),abs(b2-a1)))

else:
    print(0)