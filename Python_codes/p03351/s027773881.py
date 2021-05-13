a,b,c,d = map(int,input().split())

d1 = abs(a-b)
d2 = abs(b-c)
d3 = abs(a-c)

if ((d3 <= d)or((d1 <= d)and(d2 <= d))):
    print("Yes")
else:
    print("No")
