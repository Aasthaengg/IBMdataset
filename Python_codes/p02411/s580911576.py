result = []
m,f,r=[int(x) for x in input().split()]
while not m==f==r==-1:
    if (m == -1 or f == -1):
        res = "F"
    elif (m + f >= 80):
        res = "A"
    elif (65 <= m + f < 80):
        res = "B"
    elif (50 <= m + f < 65):
        res = "C"
    elif (30 <= m + f < 50):
        res = "D"
        if (50 <= r):
            res = "C"
    else :
        res = "F"
    result.append(res)
    m,f,r=[int(x) for x in input().split()]
for i in result:
    print(i)