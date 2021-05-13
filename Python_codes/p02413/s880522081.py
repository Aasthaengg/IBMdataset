def show2dlist(nlist,r,c):
    for x in xrange(0,r):
        nlist[x] = map(str,nlist[x])
        ans = " ".join(nlist[x])
        print ans
def showlist(nlist,nlistlen):
    for x in xrange(nlistlen):
        print nlist[x],

r,c = map(int,raw_input().split())
table = [[0 for x in xrange(c)] for y in xrange(r)]
i = 0
for x in xrange(r):
    table[i] = map(int,raw_input().split())
    i+=1
# calc table
csumlist =[0 for x in xrange(0,c+1)]
for x in xrange(0,r):
    table[x].append(sum(table[x]))
    for y in xrange(0,c+1):
        csumlist[y] += table[x][y]
show2dlist(table,r,c+1)
showlist(csumlist,c+1)