[a,b,c] = raw_input().split(' ')
a = int(a)
b = int(b)
c = int(c)
t = 0
if a > b:
    t = a
    a = b
    b = t
if b > c:
    t = b
    b = c
    c = t
if a > b:
    t = a
    a = b
    b = t
print a,b,c