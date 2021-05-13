datos=input().split()
d12=int(datos[0])
d13=int(datos[1])
d23=int(datos[2])
#Comenzado por ciudad 1
dm=d12+d23
dm1=d13+d12
dm2=d13+d23
if dm<=dm1 and dm<=dm2:
    print(str(dm))
elif dm1<=dm and dm1<=dm2:
    print(str(dm1))
elif dm2<=dm and dm2<=dm1:
    print(str(dm2))