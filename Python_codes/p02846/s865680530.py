t1, t2 = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

c = 0
c += a1*t1-b1*t1
c += a2*t2-b2*t2

#print(c)
if c == 0:
    print('infinity')
    exit()

if c > 0:
    if b1*t1-a1*t1 < 0:
        ans = 0
    else:
        q, r = divmod(b1*t1-a1*t1, c)
        if r == 0:
            ans = 2*q
        else:
            ans = 2*q+1
else:
    c *= (-1)
    if -b1*t1+a1*t1 < 0:
        ans = 0
    else:
        q, r = divmod(-b1*t1+a1*t1, c)
        if r == 0:
            ans = 2*q
        else:
            ans = 2*q+1
print(ans)
