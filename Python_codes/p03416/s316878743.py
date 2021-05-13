a,b = map(int,input().split())
c = str(a)
d = str(b)
e = 0
f = 0
if int(c[0]) + int(c[1]) * 10 >= int(c[3]) * 10 + int(c[4]):
    e = a // 100
else:
    e = a // 100 + 1
if int(d[0]) + int(d[1])*10 <= int(d[3])*10 + int(d[4]):
    f = b // 100
else:
    f = b // 100 - 1
print(f-e+1)