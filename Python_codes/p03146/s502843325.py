s = int(input())
an = [s]
for n in range(2, 1000):
    if an[n-2]%2 == 0:
        a = an[n-2]//2
        #print(a)
        if a in an:
            print(n)
            exit()
        else:
            an.append(a)
    else:
        a = 1 + 3*an[n-2]
        if a in an:
            print(n)
            exit()
        else:
            an.append(a)