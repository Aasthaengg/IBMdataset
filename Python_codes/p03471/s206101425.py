din = list(map(int,input().split()))
NN = din[0]
YY = din[1]

found = 0
for n10000 in range(NN+1):
    if found == 1: break
    n_rem = NN - n10000
    n5000 = 0
    while ((n5000<=n_rem) and (found == 0)):
        n1000 = NN-n10000-n5000
        if YY - n10000*10000 - n5000*5000 - n1000*1000 == 0:
            line = "{} {} {}".format(n10000,n5000,n1000)
            print(line)
            found = 1;
        else:
            n5000 += 1
if found == 0:
    print("-1 -1 -1")