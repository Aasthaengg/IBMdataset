n=list(map(int,input().split()))
a= str(n[0])+str(n[1])+str(n[2])
maiden=0;z=0;iguales=4504501;iguales_2=1127251;iguales_3=2253001
if(n[0]==1 and n[1]==1 and n[2]==1):
    for k in range(3000-n[3]):
        iguales = iguales-(3001-k)
    print(iguales)
elif(n[0]==2 and n[1]==2 and n[2]==2):
    if(n[3]%2==0):
        for k in range(int((3000-n[3])/2)):
            iguales_2 = iguales_2-(1501-k)
        print(iguales_2)
    else:
        print(0)
elif(a=='121'or a=='112' or a=='211' and n[3]>=2997):
    for k in range(int(3000 -n[3])):
            iguales_3 = iguales_3-(1501-k)
    print(iguales_3)
else:
    for i in range((n[3]//n[0])+1):
        for j in range((n[3]//n[1])+1):
            z=(n[3]-i*n[0]-j*n[1])/n[2]
            if(z%1==0 and z>=0):
                maiden=maiden+1    
    print(maiden)