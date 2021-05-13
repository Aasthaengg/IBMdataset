a = []
while True:
    tmp = input()
    if tmp == 0:
        break
    a.append(tmp)
for x in xrange(0,len(a)):
    print "Case "+str(x+1)+": " + str(a[x])