w,a,b = map(int,input().split())

if a==b or a<b and b<=a+w or b<a and a<=b+w:
    print(0)
else:
    print(min(abs(a+w-b),abs(b+w-a)))