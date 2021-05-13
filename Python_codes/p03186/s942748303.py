a,b,c = map(int,raw_input().split())

if c == 0:
    print(b)
elif a >= c:
    print(b+c)
elif a+b >= c:
    print(b+c)
else:
    print(b+a+b+1)