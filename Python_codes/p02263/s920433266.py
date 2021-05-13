s=input()
d=s.split()

operater=["+","*","-","/"]
cal=[]
k=0
for i in range(len(d)):
    if d[i] not in operater:
        cal.append(int(d[i]))
        k+=1
    else:
        j=operater.index(d[i])
        if j==0:
            x=cal[k-1]+cal[k-2]
        elif j==1:
            x=cal[k-1]*cal[k-2]
        elif j==2:
            x=cal[k-2]-cal[k-1]
        else:
            x=cal[k-2]/cal[k-1]
        cal.pop()
        cal.pop()
        cal.append(x)
        print
        k-=1
print(cal[0])
