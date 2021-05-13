[a,b,c,d] = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)

if a >= 0 and c >= 0:
    print(b*d)
elif b <= 0 and d <= 0:
    print(a*c)
elif a >= 0 and d <= 0:
    print(a*d)
elif b <= 0 and c >= 0:
    print(b*c)

elif a <= 0 and b >= 0 and c <= 0 and d >= 0:
    a_c = a*c
    b_d = b*d
    if a_c >= b_d:
        print(a_c)
    else:
        print(b_d)

elif a <= 0 and b >= 0 and d <= 0:
    print(a*c)

elif a <= 0 and b >= 0 and d >= 0:
    print(b*d)

elif b <= 0 and c <= 0 and d >= 0:
    print(a*c)

elif b >= 0 and c <= 0 and d >= 0:
    print(b*d)



