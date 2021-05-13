[a,b,c,d]=[int(input()) for i in range(1,4+1)]
a1 = d // 500
b1 = d// 100
c1 = d// 50
coun = 0
for i in range(0,min([a+1,a1+1])):
    a = 500*i
    if a == d:
        coun = coun +1
        break
    for j in range(0,min([b+1,b1+1-5*i])):
        s = a + 100*j
        if s == d :
            coun = coun +1
            break
        for k in range(0,min([c+1,c1+1-10*i-2*j])):
            v = s + 50*k
            if v == d :
                coun = coun+1
                break
print(coun)