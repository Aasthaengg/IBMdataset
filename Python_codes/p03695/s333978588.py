N=int(input())
a=list(map(int,input().split()))
zako=set()
aka=list()
for i in a:
    if 1<= i <=399:
        zako.add('g')
    elif 400<=i<=799:
        zako.add('Br')
    elif 800<=i<=1199:
        zako.add('gre')
    elif 1200<=i<=1599:
        zako.add('mizu')
    elif 1600<=i<=1999:
        zako.add('blu')
    elif 2000<=i<=2399:
        zako.add('ye')
    elif 2400<=i<=2799:
        zako.add('ora')
    elif 2800<=i<=3199:
        zako.add('red')
    else:
        aka.append(1)
if len(zako)==0:
    print(1,len(aka))
else:
    print((len(zako)),(len(zako)+len(aka)))
    
