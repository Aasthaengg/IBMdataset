n=int(input())
x=[10000]*(n+2)
x[0]=0
a=[6**i for i in range(1,7)]
b=[9**i for i in range(1,6)]
c=[1]
c=a+b+c
c.sort()
for i in range(1,n+2):
    for j in c:
        if i-j>=0:
            x[i]=min(x[i],x[i-j]+1)
        else:
            break
print(x[n])