A = int ( input () )
B = int ( input () )
C = int ( input () )
x = int ( input () )
o = 0
a = A
while a >= 0:
    b = B
    while b >= 0:
        c = C
        while c >= 0:
            m = 500*a + 100*b + 50*c
            if x == m:
                o += 1
            c -= 1
        b -= 1
    a -= 1
print (o)