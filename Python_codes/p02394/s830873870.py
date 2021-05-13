W,H,x,y,r = raw_input().split()
W,H,x,y,r = map(int,(W,H,x,y,r))
def isXok(W,H,x,y,r):
    if x-r<0 or x+r>W:
        return False
    else:
        return True
def isYok(W,H,x,y,r):
    if y-r<0 or y+r>H:
        return False
    else:
        return True
if isXok(W,H,x,y,r) and isYok(W,H,x,y,r):
    print "Yes"
else:
    print "No"