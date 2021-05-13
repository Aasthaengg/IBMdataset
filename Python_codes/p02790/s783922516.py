a,b = map(int,input().split())
sa = a
sb = b

for i in range(b - 1):
    sa = sa * 10 + a

for i in range(a - 1):
    sb = sb * 10 + b

if a <= b:
    print(sa)
else:
    print(sb)