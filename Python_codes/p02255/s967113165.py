def printlist(al):
    print " ".join(map(str,al))
        

l = input()
al = map(int,raw_input().split())
printlist(al)
for i in xrange(1,l):
    v = al[i]
    j = i-1
    while j >= 0 and al[j]>v:
        al[j+1] = al[j]
        j-=1
    al[j+1]=v
    printlist(al)