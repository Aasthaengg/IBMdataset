import math
n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
D=[0,0,0,0]
p=[1,2,3]
for k in range(4):
    if k==3:
        D[k]=max(abs(x[i]-y[i])for i in range(n))
    else:
        D[k]=math.pow(sum(abs((x[i]-y[i])**p[k])for i in range(n)),1/p[k])
    print("{:.6f}".format(D[k]))

