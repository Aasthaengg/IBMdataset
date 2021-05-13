def splitcount(l):
    if len(l) == 0:
        return 0
    minl = min(l)
    #print("l",l)
    if minl==0:
        #print("l[:max(0,l.index(0))]",l[:max(0,l.index(0))])
        #print("splitcount(l[l.index(0)+1:])",splitcount(l[l.index(0)+1:]))
        return splitcount(l[:l.index(0)]) + splitcount(l[l.index(0)+1:])
    else:
        return minl + splitcount(list(map(lambda x: x - minl, l)))

n = int(input())
h = list(map(int,input().split()))


print(splitcount(h))    
