while True:
    h,w = map(int,raw_input().split())
    if h==0 and w==0:
        break
    oddlist = ["#","."]
    evenlist = [".","#"]

    for i in xrange(0,h):
        line=""
        for j in xrange(0,w):
            if i%2==0:
                line+=oddlist[j%2]
            else:
                line+=evenlist[j%2]
        print line
    print