a,b,c = map(int,input().split())
d = a - b
if d >= c:
    print(0)
else:
    print(abs(d - c))