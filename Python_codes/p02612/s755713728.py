n=int(input())

x=1000-(n%1000)

if (n%1000)==0:
    print(0)
else :
    print('{}'.format(x))