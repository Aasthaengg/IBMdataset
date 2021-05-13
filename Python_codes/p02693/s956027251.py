x=int(input())
y=input()
z=y.split(" ")
a=int(z[0])
b=int(z[1])
over=0
multiples=[x*d for d in range(1000)]
for c in multiples:
    if(over==0):
        if(c>=a and c<=b):
            print('OK')
            over+=1
if(over==0):
    print('NG')