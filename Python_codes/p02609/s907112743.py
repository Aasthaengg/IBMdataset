def func(z,c):
    if c == 0:
        z = 0
    else:
        z = z%c
    a = bin(z)
    b = 0
    for i in range(len(a)):
        if a[i] == "1":
            b += 1
    return z,b

n = int(input())
x = input()
c = 0
for i in range(n):
    if x[i] == "1":
        c += 1
s0 = int(x,2)%(c+1)
if c <= 1:
    s1 = 0
else:
    s1 = int(x,2)%(c-1)
for i in range(n):
    sw = 0
    if x[i] == "0":
        d = c + 1
        z = (s0 + pow(2,n-i-1,d))%d
    else:
        d = c - 1
        if d == 0:
            z = 0
            sw = 1
        else:
            z = (s1 - pow(2,n-i-1,d))%d
    ans = 1
    p = bin(z)
    e = 0
    for A in str(p):
        if A == "1":
            e += 1
    d = e
    if sw == 1:
        ans = 0
    else:
        while z:
            z,d = func(z,d)
            ans += 1
    print(ans)