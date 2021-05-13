a=[0 for i in range(10**5+3)]
b=[1 for i in range(10**5+3)]
for i in range(2,10**5+3):
    if b[i]==1:
        for j in range(2*i,10**5+3,i):
            b[j]=0
b[0]=0
b[1]=0
for i in range(1,10**5+3,2):
    a[i]=b[i] and b[(i+1)//2]
e=[a[0]]
for i in range(1,10**5+3):
    e.append(a[i]+e[i-1])
#print(e)
for i in range(int(input())):
    l,r=map(int,input().split())
    print(e[r]-e[l-1])