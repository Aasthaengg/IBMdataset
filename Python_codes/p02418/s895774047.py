ringstr = raw_input()
matchstr = raw_input()

ringstrlen = len(ringstr)
matchstrlen = len(matchstr)
x = 0 # match length
y = 0 # ring length
hitflag = False
finflag = False
while True:
    if x == matchstrlen:
        print "Yes"
        break
    if y == ringstrlen:
        y=0
        finflag =True
    if matchstr[x]==ringstr[y]:
        x+=1
        if not hitflag:
            tmpy = y
            hitflag = True
        y+=1
    else:
        if hitflag:
            hitflag = False
            if finflag:
                print "No"
                break
            x=0
            y=tmpy+1
            continue
        else:
            if y == ringstrlen-1:
                print "No"
                break
            y+=1