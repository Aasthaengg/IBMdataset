sixexp=[6**i for i in range(1,7)]
nineexp=[9**i for i in range(1,6)]
lis=[1]+sixexp+nineexp

n=int(input())

F=[0,1]

for i in range(2,n+1):
    dplis=[]
    for j in lis:
        if i-j>=0:
            dplis.append(F[i-j]+1)
    F.append(min(dplis))

print(F[n])