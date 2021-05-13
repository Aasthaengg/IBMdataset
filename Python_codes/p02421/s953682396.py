n = int(raw_input())
ts=0 #taro score
hs=0 #hanako score
for x in xrange(n):
    #tc:taro card/hc:hanako card
    tc,hc = raw_input().split()
    if tc > hc:
        ts += 3
    elif tc < hc:
        hs += 3
    else:
        ts += 1
        hs += 1
print "%d %d"%(ts,hs)