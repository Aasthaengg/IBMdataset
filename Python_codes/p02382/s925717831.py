import math
n=int(input())
x=[float(a) for a in input().split()]
y=[float(b) for b in input().split()]
p=[float(1),float(2),float(3),math.inf]
for j in range(3):
    lst=[]
    for i in range(n):
        if x[i]>=y[i]:
            s=(x[i]-y[i])**(p[j])
        else:
            s=(y[i]-x[i])**(p[j])
        lst.append(s)
    t=sum(lst)
    print(f'{t**(1/p[j]):10.8f}')
lst1=[]
for k in range(n):
    if x[k]>=y[k]:
        u=x[k]-y[k]
    else:
        u=y[k]-x[k]
    lst1.append(u)
print(f'{max(lst1):10.8f}')
        

