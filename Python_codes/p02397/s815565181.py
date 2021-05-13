i = 0
while 1:
        w  = map(int,raw_input().split())
        w.sort()
        if w[0] == 0 and w[1] == 0:
                break
        print "%d %d" %(w[0],w[1])