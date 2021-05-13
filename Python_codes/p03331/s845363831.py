n = int(input())

l = []
for i in range(1, n):
    a = i
    b = n - i
    ra = 0
    rb = 0

    flg = True
    while flg:
        aa = a % 10
        a //= 10
        ra += aa
        if a == 0:
            flg = False
    flg = True
    while flg:
        bb = b % 10
        b //= 10
        rb += bb
        if b == 0:
            flg = False
    l.append(ra+rb)
print(min(l))