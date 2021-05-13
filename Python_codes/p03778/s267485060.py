w,a,b = map(int,input().split())
a1 = a+w
b1 = b+w
x = min(a,b)

if x == a:
    ans = b-a1
elif x == b:
    ans = a-b1

if ans <0:
    print(0)
else:
    print(ans)
