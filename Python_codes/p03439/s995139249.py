N=int(input())
l,r=0,N
print(0)
s=input()
ls=s
if s!='Vacant':
    for i in range(19):
        x=l+(r-l)//2
        print(x)
        s=input()
        if s=='Vacant':
            break
        elif (x-l)%2==0 and s==ls or (x-l)%2==1 and s!=ls:
            l=x
            ls=s
        else:
            r=x
