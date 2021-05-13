s = int(input())
p = 10 ** 9
xp = s % p
yp = s // p
x = p - xp
y = yp + 1

if s != 10 ** 18:
    print(0,0,p,1,x,y)
else:
    print(0,0,p,0,0,p)