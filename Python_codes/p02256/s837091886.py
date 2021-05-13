def gdc(a,b):
    #print("%d, %d"%(a,b))
    if min(a,b) == 0:
        return a
    else:
        return gdc(min(a,b), max(a,b)%min(a,b))
        
a = [int(s) for s in input().split(" ")]
print(gdc(a[0],a[1]))