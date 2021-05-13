test = []
while True:
    tmp = map(int,raw_input().split())
    if tmp[0]==tmp[1]==tmp[2]==-1:
        break
    else:
        test.append(tmp)
for a in test:
    if a[0] == -1 or a[1] == -1:
        print "F"
    elif a[0]+a[1] >= 80:
        print "A"
    elif 80 > a[0]+a[1] >= 65:
        print "B"
    elif 65 > a[0]+a[1] >= 50:
        print "C"
    elif 50 > a[0]+a[1] >= 30:
        if a[2] >= 50 and 50 > a[0]+a[1] >= 30:
            print "C"
        else:
            print "D"
    elif a[0] + a[1] < 30:
        print "F"