x,n=map(int,input().split())
datap=[int(i) for i in input().split()]

for i in range(x-n-1,x+1,1):
    if i in datap:
        pass
    else:
        ansm=i

for j in range(x+n+1,x-1,-1):
    if j in datap:
        pass
    else:
        ansp=j

if x-ansm>ansp-x:
    print(ansp)
else:
    print(ansm)