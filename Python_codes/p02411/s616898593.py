
x = raw_input()
m, f, r = x.split()
m = int(m)
f = int(f)
r = int(r)

while m != -1 or f != -1 or r != -1:
    sum = m + f
    if (m == -1 or f == -1) or sum < 30:
        print "F"
    elif sum >= 80:
        print "A"
    elif 80 > sum and sum >= 65:
        print "B"
    elif 65 > sum and sum >= 50:
        print "C"
    elif 50 > sum and sum >= 30:
        if r < 50:
            print "D"
        else:
            print "C"
            
    x = raw_input()
    m, f, r = x.split()
    m = int(m)
    f = int(f)
    r = int(r)