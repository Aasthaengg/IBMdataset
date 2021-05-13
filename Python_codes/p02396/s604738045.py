i=int(input())
l=[]
while i!=0:
    l.append(i)
    i=int(input())
for d in range(len(l)):
    print "Case "+str(d+1)+": "+str(l[d])
