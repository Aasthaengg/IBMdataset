a,b=(int(x) for x in input().split())
c = a + b
if c < 10:
    print(c)
elif c >= 10:
    print('error')