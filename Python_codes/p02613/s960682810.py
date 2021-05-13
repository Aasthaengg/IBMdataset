N=int(input())
d=[input() for i in range(N)]
ac=0
wa=0
tle=0
re=0
for i in range(N):
    if d[i]=="AC":
        ac+=1
    elif d[i]=="WA":
        wa+=1
    elif d[i]=="TLE":
        tle+=1
    else:
        re+=1
print("AC x "+str(ac))
print("WA x "+str(wa))
print("TLE x "+str(tle))
print("RE x "+str(re))