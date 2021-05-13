N = int(input())
lowid= 0
highid = N-1
print(0)
lowsex = input()
if lowsex=='Vacant':
    exit()
print(N-1)
highsex = input()
if highsex=='Vacant':
    exit()
while highid-lowid>1:
    midid = (lowid+highid)//2
    print(midid)
    midsex = input()
    if midsex=='Vacant':
        exit()
    if (midid-lowid)%2==1 and midsex==lowsex:
        highid = midid
        highsex = midsex
    elif (midid-lowid)%2==0 and midsex!=lowsex:
        highid = midid
        highsex = midsex
    else:
        lowid = midid
        lowsex = midsex