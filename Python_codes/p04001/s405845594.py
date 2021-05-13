s=input()
ls=len(s)

sl=[]
for i in range(ls):
    sl.append(s[i])
nl=[int(j) for j in sl]

#"+"が入りうる箇所はls-1箇所ある
sumn=[]
#i=0~3
#i=0x00,0x01,0x10,0x11
for i in range(2**(ls-1)):
    #j=0~1
    mul=1
    for j in range(ls-1):
        number=mul*nl[ls-j-1]
        if ((i>>j)&1):
            mul=1
        else:
            mul*=10
        sumn.append(number)
    sumn.append(nl[0]*mul)
print(sum(sumn))
