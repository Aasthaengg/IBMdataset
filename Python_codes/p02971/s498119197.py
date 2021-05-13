n=int(input())
a=[]
am,amm=0,0
for i in range(n):
    x=int(input())
    if x>am:
        am,amm=amm,x
    elif x>amm:
        amm=x
    a.append(x)
for i in range(n):
    if a[i]==am:
        print(amm)
    else:
        print(am)