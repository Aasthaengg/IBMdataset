while True:
    n=list((raw_input()))
#    n=list(int(raw_input()))
    if int(n[0]) == 0:
        break
    else:
        x=0
        for i in xrange(len(n)):
            x+=int(n[i])
    print x