n,a,b = map(int,input().split())
t = True
if a > b:
    t = False
if a != b and n == 1:
    t = False
if t:
    if n == 1 or n == 2:
        print(1)
    else:
        print((b*(n-1)+a)-(a*(n-1)+b)+1)
else:
    print(0)