

def p(k,w,maxP):
    count = 1
    tmpWeight = 0
    for x in w:
        if tmpWeight+x <= maxP:
            tmpWeight += x
        else:
            count += 1
            if count > k :
                return False
            tmpWeight = x
    

    return True




n,k = map(int,input().split())


w = []

for _ in range(n):
    w.append((int)(input()))
rangeMax = sum(w)
rangeMin = max(w)
rangeMid = 0
while rangeMin < rangeMax:
    rangeMid = (rangeMax + rangeMin)//2
    '''print(p(k,w,rangeMid))
    print(p(k,w,rangeMid+1))
    print("---")
    '''
    if p(k,w,rangeMid) == True:
        rangeMax = rangeMid
    else:
        rangeMid += 1
        rangeMin = rangeMid

print(rangeMid)